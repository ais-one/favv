from redis import Redis
from rq import Queue, Worker
from rq.command import send_shutdown_command # send_stop_job_command, send_kill_horse_command
# from rq.worker import Worker

worker=None

def rq_start():
  redis = Redis()
  queue = Queue('queue_name')
  # Start a worker with a custom name
  worker = Worker([queue], connection=redis, name='foo')

def rq_stop():
  redis = Redis()
  workers = Worker.all(redis)
  for worker in workers:
    send_shutdown_command(redis, worker.name)  # Tells worker to shutdown