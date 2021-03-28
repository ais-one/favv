import subprocess
from fastapi import APIRouter

from redis import Redis

from services.model import get_model_folder, set_model_path # reference favv/fastapi/app
from services.db import get_db # reference favv/fastapi/app

from .uploads import router_custom_app_uploads # reference same level
from .s3 import router_custom_app_s3 # reference same level
from .cascade import router_custom_app_cascade # reference same level

# from .models.huey_config import huey - TBD use config...
from huey import RedisHuey
huey = RedisHuey('test', blocking=False)
from .models.tasks import add_numbers

import numpy as np

router_custom_app = APIRouter(prefix="/custom-app")

router_custom_app.include_router(router_custom_app_uploads)
router_custom_app.include_router(router_custom_app_s3)
router_custom_app.include_router(router_custom_app_cascade)

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

@router_custom_app.get("/huey-get-test", tags=["api_custom_app"])
async def huey_get_test():
  # pending = huey.pending()
  # num_pending = len(pending)
  num_scheduled = huey.__len__()
  return { "pending tasks": num_scheduled }
