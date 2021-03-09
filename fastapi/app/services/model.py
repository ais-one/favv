import os
from config import get_settings

def get_model_folder():
  realpath = os.path.dirname( os.path.realpath(__file__) )
  file_path = os.path.abspath( os.path.join(realpath, "..", get_settings().APP, get_settings().MODEL_FOLDER) ) # relative to app
  print(file_path)
  return file_path

def set_model_path(filename: str):
  realpath = os.path.dirname( os.path.realpath(__file__) )
  file_path = os.path.abspath( os.path.join(realpath, "..", get_settings().APP, get_settings().MODEL_FOLDER, filename) ) # relative to app
  return file_path
