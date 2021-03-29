import dramatiq

from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="127.0.0.1")
dramatiq.set_broker(redis_broker)
