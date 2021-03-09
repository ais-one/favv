import shutil
import os
from fastapi import APIRouter, File, UploadFile, Query
from fastapi.responses import FileResponse # from starlette.responses import FileResponse
from typing import List

# this is referencing fastapi/app...
from services.file import get_upload_folder, set_upload_path, list_files

router_sample_app_uploads = APIRouter(
  tags=["sample-app-uploads"],
  prefix="/uploads"
)

## Upload folder

@router_sample_app_uploads.get("/ext-upload-folder")
async def ext_upload_folder():
  return { "Upload Folder": get_upload_folder() }

@router_sample_app_uploads.get("/ext-list-files")
async def ext_list_files():
  files = list_files()
  return { "files": files }

@router_sample_app_uploads.delete("/ext-delete-file")
async def ext_delete_file(filename: str = Query(None)):
  file_path = set_upload_path(filename)
  try:
    if os.path.exists(file_path):
      os.remove(file_path)
      return {"status": "deleted"}
    return {"status": "cannot delete"}
  except:
    return {"status": "delete error"}

@router_sample_app_uploads.post("/ext-upload-save")
async def ext_upload_save(image: UploadFile = File(...)):
  file_path = set_upload_path(image.filename)
  with open(file_path, "wb") as buffer: # it saves to fastapi/app folder... how to specify another folder
    shutil.copyfileobj(image.file, buffer)
  return {"filename": image.filename}

@router_sample_app_uploads.post("/ext-upload-see-data")
async def ext_upload_see_data(image: UploadFile = File(...)):
  file_data =  image.file.read()
  try:
    file_data = file_data.decode()
    return {"file_data": file_data } # text
  except (UnicodeDecodeError, AttributeError):
    return {"file_data": image.content_type } # byte "application/pdf"

@router_sample_app_uploads.post("/ext-upload-multi")
async def ext_upload_save_multi(images: List[UploadFile] = File(...)):
  for image in images:
    file_path = set_upload_path(image.filename)
    with open(file_path, "wb") as buffer:
      shutil.copyfileobj(image.file, buffer)
  return {"status": "uploaded"}

@router_sample_app_uploads.get("/ext-read-file")
async def ext_read_file(filename: str = Query(None)):
  file_path = set_upload_path(filename)
  with open(file_path, "rb") as buffer: # it saves to fastapi/app folder... how to specify another folder
    try:
      file_data = buffer.read()
      file_data = file_data.decode()
      return {"file_data": file_data } # text
    except (UnicodeDecodeError, AttributeError):
      return {"file_data": "Its Binary" }

@router_sample_app_uploads.get("/ext-download-file")
async def ext_download_file(filename: str = Query(None)):
  file_path = set_upload_path(filename)
  return FileResponse(file_path, media_type='application/octet-stream',filename="down-"+filename)
