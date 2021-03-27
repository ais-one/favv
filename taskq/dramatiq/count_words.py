from time import sleep
import dramatiq
# import requests

from dramatiq import actor, set_broker
from dramatiq.brokers.redis import RedisBroker
set_broker(RedisBroker())

def should_retry(retries_so_far, exception):
  return retries_so_far < 3 and isinstance(exception, HttpTimeout)
# min_backoff
# max_backoff
# throws
# max_age
# time_limit
# @dramatiq.actor(max_retries=3)
# @dramatiq.actor(retry_when=should_retry)
# def count_words(url):
#   response = requests.get(url)
#   count = len(response.text.split(" "))
#   print(f"There are {count} words at {url!r}.")

@dramatiq.actor
def count_words():
  print("model started")
  sleep(5) # Time in seconds
  print("model completed")

# from dramatiq.middleware import TimeLimitExceeded

# @dramatiq.actor(time_limit=1000)
# def long_running():
#     try:
#         setup_missiles()
#         time.sleep(2)
#         launch_missiles()    # <- this will not run
#     except TimeLimitExceeded:
#         teardown_missiles()  # <- this will run

# def main(args):
# count_words.send()

if __name__ == "__main__":
  print('in __main__')
  count_words.send()
  #     sys.exit(main(sys.argv))