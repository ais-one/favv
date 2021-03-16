import shutil
from fastapi import APIRouter, File, UploadFile, Query
from fastapi.responses import FileResponse # from starlette.responses import FileResponse
from typing import List

# this is referencing fastapi/app...
from services.s3 import get_s3, get_s3_bucket_name

router_custom_app_s3 = APIRouter(
  tags=["custom_app_s3"],
  prefix="/s3"
)

## S3 buckets

@router_custom_app_s3.get("/ext-list-s3-buckets")
async def ext_list_buckets():
  try:
    s3buckets = None
    s3obj = get_s3()
    if s3obj != None:
      res = s3obj.list_buckets()
      if res != None:
        s3buckets = res["Buckets"]
        # print("Buckets")
        # for bucket in res["Buckets"]:
        #     print(f"  {bucket["Name"]}")
    return { "Buckets": s3buckets }
  except:
    return { "Error": "List Buckets Error" }

@router_custom_app_s3.get("/ext-list-s3-files")
def ext_list_objects():
  bucket_name=get_s3_bucket_name()
  files=[]
  try:
    objs = get_s3().list_objects_v2(Bucket=bucket_name, MaxKeys=500)
    for obj in objs["Contents"]:
      files.append(obj["Key"])
    return files
  except:
    return { "Error": "List" }

@router_custom_app_s3.post("/ext-upload-s3-file")
def ext_upload_file(image: UploadFile = File(...)):
  bucket_name=get_s3_bucket_name()
  try:
    # f = open("guru99.txt","rb")
    # s3.upload_fileobj(f, BUCKET_NAME, 'aaa/vvv.txt')
    # f.close()
    get_s3().upload_fileobj(image.file, bucket_name, image.filename)
    return { "Status": "Ok" }
  except:
    return { "Error": "Upload" }

@router_custom_app_s3.delete("/ext-delete-s3-file")
def ext_delete_file(object_key: str = Query(None)):
  bucket_name=get_s3_bucket_name()
  try:
    res = get_s3().delete_object(Bucket=bucket_name, Key=object_key)
    return { "Status": "Ok", "Response": res }
  except:
    return { "Error": "Delete" }

@router_custom_app_s3.get("/ext-read-s3-file")
def ext_read_file(object_key: str = Query(None)):
  bucket_name=get_s3_bucket_name()
  try:
    res = get_s3().get_object(Bucket=bucket_name, Key=object_key)
    data_str = res['Body'].read().decode('utf-8')
    # TBD handle binary data
    # TBD save to file
    # with open('output.txt', 'wb') as data:
    #     s3.download_fileobj(BUCKET_NAME, 'aaa/vvv.txt', data)
    return { "Status": "Ok", "Data": data_str }
  except:
    return { "Error": "Read" }
