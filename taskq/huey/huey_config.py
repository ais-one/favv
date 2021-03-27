from huey import RedisHuey # MemoryHuey
huey = RedisHuey('test', blocking=False)
