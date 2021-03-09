import os
from config import get_settings

def get_upload_folder():
  realpath = os.path.dirname( os.path.realpath(__file__) )
  file_path = os.path.abspath( os.path.join(realpath, "..", get_settings().APP, get_settings().UPLOAD_FOLDER) ) # relative to app
  print(file_path)
  return file_path

def set_upload_path(filename: str):
  realpath = os.path.dirname( os.path.realpath(__file__) )
  file_path = os.path.abspath( os.path.join(realpath, "..", get_settings().APP, get_settings().UPLOAD_FOLDER, filename) ) # relative to app
  return file_path

def list_files():
  mypath = get_upload_folder()
  onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
  return onlyfiles