from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["api-demo-exceptions"], prefix="/exceptions")

items = {"foo": "The Foo Wrestlers"}

@router.get("/excp-items/{item_id}")
async def excp_read_items(item_id: str):
  if item_id not in items:
    raise HTTPException(
      status_code=404,
      detail="Item not found",
      headers={"X-Error": "There goes my error"} # add custom headers
    )
  return {"item": items[item_id]}

# @app.exception_handler(StarletteHTTPException)
@router.get("/excp-items2/{item_id}")
async def excp_read_items2(item_id: int):
  if item_id == 3:
    raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
  return {"item_id": item_id}


class Item4(BaseModel):
  title: str
  size: int

# @app.exception_handler(RequestValidationError)
@router.post("/excp-items3/", description="set size to an integer to see error")
async def excp_read_items3(item: Item4):
  return item