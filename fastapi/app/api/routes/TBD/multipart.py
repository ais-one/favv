# test out multipart forms
from fastapi import APIRouter, Form, File, UploadFile
from typing import List

import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This message should go to the log file")
# logging.info("So should this")
# logging.warning("And this, too")
# logging.error("And non-ASCII stuff, too, like Øresund and Malmö")

router = APIRouter(tags=["api-demo-multipart"], prefix="/multipart")

@router.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
  return {"username": username}

# single files first
@router.post("/files/")
async def create_file(file: bytes = File(...)): # store all in memory
  return {"file_size": len(file), "content": file}

# https://www.starlette.io/requests/#request-files
@router.post("/uploadfile/") # streaming
async def create_upload_file(file: UploadFile = File(...)):
  contents = await file.read()
  # logging.warning("BLAH2 %s", file)
  logging.warning("BLAH3 %s", contents)
  return {"filename": file.filename}

# multiple
@router.post("/files-multi/")
async def create_files_multi(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@router.post("/uploadfiles-multi/")
async def create_upload_files_multi(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

@router.post("/files-mixed/")
async def create_file_mix(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
  return {
    "file_size": len(file),
    "token": token,
    "fileb_content_type": fileb.content_type,
  }
