from pymongo import MongoClient
from config import get_settings

import json
from bson import ObjectId

# class JSONEncoder(json.JSONEncoder):
#   def default(self, o):
#     if isinstance(o, ObjectId):
#       return str(o)
#     return json.JSONEncoder.default(self, o)

mongodb = None

def bson2dict(input):
  try:
    return json.loads(
      json.dumps(input, default=str) # convert objects to string
    ) # convert string to dict
  except:
    return None

def get_mongodb():
  global mongodb
  return mongodb

def connect_mongodb():
  try:
    global mongodb
    url = get_settings().MONGODB_URL
    name = get_settings().MONGODB_DB
    if url != "" and name != "":
      client = MongoClient(url)
      mongodb = client[name]
      print("MongoDB Connected")
    else:
      print("No MongoDB Config")
  except Exception as e:
    print("MongoDB Connect Fail: " + str(e))

def disconnect_mongodb():
  print("Close MongoDB")