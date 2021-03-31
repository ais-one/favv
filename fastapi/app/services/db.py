# import logging

# from motor.motor_asyncio import AsyncIOMotorClient
# from config import DATABASE_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
# from .mongodb import db
# Base = declarative_base()

# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
# from . import crud, models, schemas
# from .database import SessionLocal, engine
# models.Base.metadata.create_all(bind=engine)
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_settings
import logging

logger = logging.getLogger(__name__)
logger.warn("Logging @ %s", __name__)

class Database:
  client = None

db = Database()

def get_db():
  return db.client()

def connect_db():
  try:
    url = get_settings().SQLALCHEMY_DB_URL # "sqlite:///./dev.sqlite3"
    if url != "":
      # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
      engine = create_engine(url, connect_args={"check_same_thread": False})
      db.client = sessionmaker(autocommit=False, autoflush=False, bind=engine)
      print("DB Connected")
    else:
      print("No DB Config")
  except Exception as e:
    print("DB Connect Fail: " + str(e))

def disconnect_db():
  print("Close DB v2")