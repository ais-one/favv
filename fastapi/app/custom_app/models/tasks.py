import os
from config import get_settings # can use stuff from framework...

from huey import RedisHuey
huey = RedisHuey('test', blocking=False)

# from huey_config import huey # TOREMOVE
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


# def task_b():
#   print('Task B Huey Demo -- adds two numbers.')
#   res = add_numbers(3, 4)
#   print(res)

# import sys
# if __name__ == '__main__':
#   print('Task A Huey Demo -- adds two numbers.')
#   res = add_numbers(1, 2)
#   id1 = res.id

#   pending = huey.pending()
#   print(len(pending))
#   for i in pending:
#     print(i.id)
#     # print(dir(i))
#     # methods = [method_name for method_name in dir(i) if callable(getattr(i, method_name))]
#     # print(methods)

#   # task_b()
#   # r1 = huey.result(id1, blocking=True, preserve=True)
#   # r2 = huey.result(id2, blocking=True, preserve=True)
#   # print(result)

#   # huey.all_results()
#   print('Done')
