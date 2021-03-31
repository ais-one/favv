
# from huey import RedisHuey
# huey = RedisHuey('test', blocking=False)

from huey import RedisHuey
from config import get_settings
huey = None

def connect_huey():
  global huey
  try:
    queue_name = get_settings().HUEY_TASK_QUEUES
    url = get_settings().HUEY_REDIS_CONNECTION
    if url != "" and queue_name !="":
      huey = RedisHuey(queue_name, url=url, blocking=False)
      print("Huey Connect")
    else:
      print("Huey No Connection ")
  except Exception as e:
    print("Huey Connect Fail: " + str(e))
  return huey


def disconnect_huey():
  print("Close Huey")

def get_huey():
  global huey
  return huey
