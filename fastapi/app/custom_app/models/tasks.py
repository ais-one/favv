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
