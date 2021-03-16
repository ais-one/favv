# from typing import Optional
# from pydantic import BaseModel
import redis # need to move this to somewhere configurable
from config import get_settings

cache = None

def connect_redis():
  try:
    global cache
    conn = get_settings().REDIS_CONNECTION
    if conn != "":
      cache = redis.Redis(host='127.0.0.1', port=6379)
      ping = cache.ping()
      if ping is True:
        print("Redis Connected")
      else:
        print("Redis Ping Failed")
    else:
      print("No Redis Config")
  except:
    print("Redis Connect Fail")

async def get_redis():
  global cache
  return cache

async def redis_set(key: str, value: str):
  try:
    global cache
    cache.set(key, value)
    return True
  except:
    return False

async def redis_delete(key: str):
  try:
    global cache
    cache.delete(key)
    return True
  except:
    return False

async def redis_get(key: str):
  try:
    global cache
    return cache.get(key)
  except:
    return False
