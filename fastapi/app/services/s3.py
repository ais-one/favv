# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
import boto3
import logging
from config import get_settings

logger = logging.getLogger(__name__)
logger.warn("Logging @ %s", __name__)

s3 = None

def connect_s3():
  try:
    url = get_settings().S3_ENDPOINT_URL
    global s3
    if url != "":
      s3 = boto3.client(
        "s3",
        endpoint_url=get_settings().S3_ENDPOINT_URL,
        aws_access_key_id=get_settings().S3_ACCESS_ID,
        aws_secret_access_key=get_settings().S3_SECRET_KEY
      )
      print("S3 Connected")
    else:
      s3 = None
      print("No S3 Config")
  except Exception as e:
    print("S3 Connect Fail: " + str(e))

def get_s3():
  global s3
  return s3

def get_s3_bucket_name():
  return get_settings().S3_BUCKETNAME

## Not Used
def create_bucket(bucket_name):
  try:
    res = s3.create_bucket(Bucket=bucket_name)
  except ClientError as e:
    print(e)
 
def delete_bucket(bucket_name):
  try:
    res = s3.delete_bucket(Bucket=bucket_name)
  except ClientError as e:
    print(e)
