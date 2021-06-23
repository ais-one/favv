import subprocess
from fastapi import APIRouter

from redis import Redis

from services.model import get_model_folder, set_model_path # reference favv/fastapi/app
from services.db import get_db # reference favv/fastapi/app

from .uploads import router_custom_app_uploads # reference same level
from .s3 import router_custom_app_s3
from .cascade import router_custom_app_cascade
from .ws import router_custom_app_ws

from services.huey_config import get_huey # task queue
from custom_app.models.tasks import add_numbers
# from .models.tasks import add_numbers # An alternative to above

import graphene # graphql
from starlette.graphql import GraphQLApp

import numpy as np

router_custom_app = APIRouter(prefix="/custom-app")

router_custom_app.include_router(router_custom_app_uploads)
router_custom_app.include_router(router_custom_app_s3)
router_custom_app.include_router(router_custom_app_cascade)
router_custom_app.include_router(router_custom_app_ws)

# graphql
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    def resolve_hello(self, info, name):
        return "Hello " + name

# graphql - http://127.0.0.1:3000/api/graphql (it did not recognize prefix... like websockets currently)
# https://fastapi.tiangolo.com/advanced/graphql/
router_custom_app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))

@router_custom_app.get("/ext-db", tags=["api_custom_app"])
async def ext_db():
  result = get_db().execute("select * from books")
  names = [row[1] for row in result]
  print(names)
  return { "Where": "ext-db", "test": names }

@router_custom_app.get("/ext-spawn", tags=["api_custom_app"])
async def ext_spawn():
  spawn_path = set_model_path("run_model.py")
  subprocess.Popen(
    ["python", spawn_path],    # program and arguments
    # stdout=subprocess.PIPE,  # capture stdout
    # check=True               # raise exception if program fails
  )
  # print(result.stdout)         # result.stdout contains a byte-string
  return { "Where": "ext-spawn", "Notes": "need something to block to prevent too many clicks on model execution" }

# from fastapi.responses import StreamingResponse
# some_file_path = "large-video-file.mp4"
# app = FastAPI()
# @app.get("/")
# def main():
#     file_like = open(some_file_path, mode="rb")
#     return StreamingResponse(file_like, media_type="video/mp4")

@router_custom_app.get("/numpy-test", tags=["api_custom_app"])
async def numpy_test():
  a = np.arange(6)
  return a.tolist()

@router_custom_app.post("/huey-post-test", tags=["api_custom_app"])
async def huey_post_test():
  print('Task Huey Demo -- adds two numbers.')
  res = add_numbers(3, 4)
  print(res)
  return { "task_run_id": res.id }

@router_custom_app.get("/huey-scheduled-test", tags=["api_custom_app"])
async def huey_scheduled_test():
  huey = get_huey()
  try:
    scheduled = huey.scheduled()
    num_scheduled = len(scheduled)
    return { "num_scheduled": num_scheduled }
  except Exception as e:
    return { "num_scheduled": str(e) }

@router_custom_app.get("/huey-pending-test", tags=["api_custom_app"])
async def huey_pending_test():
  huey = get_huey()
  try:
    pending = huey.pending() # currently this keeps failing due to not being able to find task, needs more investigation, but no a show-stopper
    num_pending = len(pending)
    return { "num_pending": num_pending }
  except Exception as e:
    return { "num_pending": str(e) }

@router_custom_app.get("/huey-get-test", tags=["api_custom_app"])
async def huey_get_test():
  huey = get_huey()
  result = []
  # list all results
  all = huey.all_results() 
  for i in all:
    id = i.decode("utf-8")
    r1 = huey.result(id, blocking=False, preserve=True) # preserve=False will clear result
    result.append({ "id": id, "result": r1 })
    # print(dir(i))
    # methods = [method_name for method_name in dir(i) if callable(getattr(i, method_name))]
  in_queue = huey.__len__()
  return {
    "items in queue": in_queue,
    "result": result
  }

@router_custom_app.delete("/huey-flush-test", tags=["api_custom_app"])
async def huey_flush():
  huey = get_huey()
  # flush results
  huey.storage.flush_results()
  return {
    "results": []
  }
