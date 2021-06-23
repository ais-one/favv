import uvicorn
from fastapi import FastAPI, Response, Request, HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from services.handlers import http_error_handler, http_422_error_handler, unicorn_exception_handler
from services.handlers import UnicornException
from services.handlers import startup_handler, shutdown_handler

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.staticfiles import StaticFiles

from api.routes.base import router

import os
import logging
# fastapi.logging = logging.getLogger("uvicorn")
from config import get_settings

tags_metadata = [
  {
    "name": "default",
    "description": "Description For Tags Metadata",
    "externalDocs": {
        "description": "Items external docs",
        "url": "https://fastapi.tiangolo.com/",
    },
  },
]

app = FastAPI(
  redoc_url=None, # do not serve redocs
  docs_url="/api-docs",
  openapi_url="/api-docs/v1/openapi.json",
  openapi_tags=tags_metadata, # for tags that need more information
  title=get_settings().APP,
  description="This is a very fancy project, with auto docs for the API and everything",
  version=get_settings().VERSION + "-" + get_settings().ENV,
)

# incoming requests to http or ws will be redirected to the secure scheme instead
# if (get_settings().USE_HTTPS == 1):
#   app.add_middleware(HTTPSRedirectMiddleware)

app.add_event_handler("startup", startup_handler)
app.add_event_handler("shutdown", shutdown_handler)

app.add_exception_handler(UnicornException, unicorn_exception_handler)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

origins = get_settings().CORS_ORIGINS.split(",") # ["http://localhost", "http://localhost:8080", "http://127.0.0.1:8080"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# set up the API
app.include_router(router, prefix="/api")

try:
  app.mount(get_settings().WEB_BASEPATH, StaticFiles(directory="static/dist", html=True), name="www")
except:
  print("Cannot mount webapp: " + get_settings().WEB_BASEPATH + " check if 'static/dist' folder exists")

print("__name__=" + __name__)

# Use uvicorn to run FastAPI app
if __name__ == "__main__":
  print("@ __main__")
  args = {
    "host": "0.0.0.0",
    "port": get_settings().API_PORT,
    "debug": True,
    "reload": True,
    "access_log": False,
    "headers": [("server", "")],
  }
  if (get_settings().USE_HTTPS == 1):
    print("Using HTTPS")
    args["ssl_keyfile"] = get_settings().HTTPS_KEY_PATH
    args["ssl_certfile"] = get_settings().HTTPS_CERT_PATH
  else:
    print("No HTTPS")
  # print(args)
  uvicorn.run("main:app", **args)

if __name__ == "__mp_main__":
  print("@ __mp_main__")

# run initialization here...???
if __name__ == "main":
  print("@ main")
  logger = logging.getLogger(__name__)
  logger.warn("ENV settings %s", get_settings().ENV)
