# import importlib
# import os
# import sys
# lib_path = os.path.abspath(os.path.join(__file__, "..", "..", "services"))
# print(lib_path)
# sys.path.append(lib_path)
# huey = getattr(importlib.import_module("huey_config"), huey)

from huey import RedisHuey
huey = RedisHuey('test', blocking=False)
# from huey_config import huey
from time import sleep

@huey.task()
def add_numbers(a, b):
  print("model started")
  sleep(5) # Time in seconds
  print("model completed")
  return a + b
