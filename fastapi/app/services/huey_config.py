from huey import RedisHuey
huey = RedisHuey('test', blocking=False)
