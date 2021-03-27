from huey import RedisHuey
huey = RedisHuey('test', blocking=False)

# from huey import MemoryHuey
# huey = MemoryHuey('test', immediate=True)
