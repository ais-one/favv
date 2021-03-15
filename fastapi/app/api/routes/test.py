# either in one file or put in folder...
from fastapi import APIRouter, Depends, Query
from typing import Optional
import subprocess
from services.db import get_db
from services.redis import get_redis

router = APIRouter(tags=["api_test"], prefix="/test")

@router.get("/another-spawn")
async def spawn_test():
  subprocess.Popen(
      ["python", "test_model.py"],    # program and arguments
      # stdout=subprocess.PIPE,  # capture stdout
      # check=True               # raise exception if program fails
  )
  # print(result.stdout)         # result.stdout contains a byte-string
  return { "Where": "test-spawn" }

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
