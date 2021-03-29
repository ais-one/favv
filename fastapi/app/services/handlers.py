from collections.abc import Iterable

from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import (
  validation_error_definition,
  validation_error_response_definition,
)
from fastapi.exceptions import RequestValidationError # override default exception handlers
from fastapi.exception_handlers import ( # check how this works
  http_exception_handler,
  request_validation_exception_handler,
)
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder # jsonable_encoder - convert a object to json

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
# from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from services.db import connect_db, disconnect_db
from services.s3 import connect_s3
from services.redis import connect_redis
from services.mongodb import connect_mongodb
from services.huey_config import connect_huey

async def startup_handler():
  print("Start Up...")
  connect_db()
  connect_s3()
  connect_redis()
  connect_mongodb()
  connect_huey()
  # db.client = AsyncIOMotorClient(DATABASE_URL, maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT)

async def shutdown_handler():
  print("Shut Down...")
  disconnect_db()

async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
  return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)

async def http_422_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
  """
  Handler for 422 error to transform default pydantic error object to gothinkster format
  """
  errors = {"body": []}
  if isinstance(exc.detail, Iterable) and not isinstance(
      exc.detail, str
  ):  # check if error is pydantic's model error
    for error in exc.detail:
      error_name = ".".join(
          error["loc"][1:]
      )  # remove 'body' from path to invalid element
      errors["body"].append({error_name: error["msg"]})
  else:
    errors["body"].append(exc.detail)
  return JSONResponse({"errors": errors}, status_code=HTTP_422_UNPROCESSABLE_ENTITY)

validation_error_definition["properties"] = {
  "body": {"title": "Body", "type": "array", "items": {"type": "string"}}
}

validation_error_response_definition["properties"] = {
  "errors": {
    "title": "Errors",
    "type": "array",
    "items": {"$ref": REF_PREFIX + "ValidationError"},
  }
}

# add custom exception handler
class UnicornException(Exception):
  def __init__(self, name: str):
    self.name = name

# @app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
  return JSONResponse( status_code=418, content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."} )
# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#   if name == "yolo":
#     raise UnicornException(name=name)
#   return {"unicorn_name": name}

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#   return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#   print(f"OMG! An HTTP error!: {repr(exc)}")
#   return await http_exception_handler(request, exc)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#   return PlainTextResponse(str(exc), status_code=400)
#   return JSONResponse(
#     status_code=422,
#     content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#   )
