import os
from config import get_settings # can use stuff from framework...
# from services.huey_config import huey

from services.huey_config import connect_huey
huey = connect_huey()

from time import sleep

@huey.task()
def add_numbers(a, b):
  realpath = os.path.dirname( os.path.realpath(__file__) )
  file_path = os.path.abspath( os.path.join(realpath, "..", get_settings().APP, get_settings().UPLOAD_FOLDER) ) # relative to app
  print(file_path)
  # print(realpath)
  # print(get_settings().UPLOAD_FOLDER)
  print("model started")
  sleep(10) # Time in seconds
  print("model completed")
  return a + b

# print('Huey Demo -- adds two numbers.')
# res = add_numbers(1, 2)
# print('Result:')
# print(res.get(True))

# import os
# if os.environ.get('WORKER_CLASS') in ('greenlet', 'gevent'):
#     print('Monkey-patching for gevent.')
#     from gevent import monkey; monkey.patch_all()
# import sys
# if __name__ == '__main__':
#   if sys.version_info[0] == 2:
#     input = raw_input
#   a = int(input('a = '))
#   b = int(input('b = '))
#   result = add(a, b)
#   print('Result:')
#   print(result.get(True))
#   print('Done')
