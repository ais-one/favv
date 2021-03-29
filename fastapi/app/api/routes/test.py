# either in one file or put in folder...
from fastapi import APIRouter, Depends, Query
from typing import Optional
import subprocess
from services.db import get_db
from services.redis import get_redis

from services.mongodb import get_mongodb, bson2dict

router = APIRouter(tags=["api_test"], prefix="/test")

@router.get("/another-db")
async def db_test():
  result = get_db().execute("select * from books")
  names = [row[1] for row in result]
  print(names)
  return { "Where": "test-another-db", "test": names }

@router.get("/redis")
async def redis_test_getset(key: str = Query(...), value: Optional[str] = Query(None)):
  try:
    cache = await get_redis()
    if value == None:
      item = cache.get(key)
      if item != None:
        item = str(item, 'utf-8')
      return { "status": item }
    else:
      cache.set(key, value)
      return { "status": "redis set" }
  except:
    return { "status": "redis test getset error" }

@router.delete("/redis")
async def redis_test_delete(key: str = Query(...)):
  try:
    cache = await get_redis()
    cache.delete(key)
    return { "status": "redis deleted" }
  except:
    return { "status": "redis test delete error" }

@router.get("/mongodb-test")
def mongodb_test():
  try:
    db = get_mongodb()
    collection = db["country"]
    result = list(collection.find({}).limit(5))
    result = bson2dict(result)
    return { "status": "mongodb", "result": result }
  except:
    return { "status": "mongodb error" }

# @app.get('/users')
# async def list_users():
#     users = []
#     for user in db.users.find():
#         users.append(User(**user))
#     return {'users': users}