from pydantic import BaseSettings
import logging
from functools import lru_cache # read .env only once

logger = logging.getLogger(__name__)
logger.warn("Logging @ %s", __name__)

import random
import string

class Settings(BaseSettings):
  ENV: str = "development"
  APP: str = "demo"
  JWT_ALG: str = "HS256"
  JWT_SECRET: str = "".join(random.choice(string.ascii_letters) for i in range(32))
  REFRESH_TOKEN_SECRET: str = "".join(random.choice(string.ascii_letters) for i in range(64))
  VERSION: str
  API_PORT=8000
  SQLALCHEMY_DB_URL: str = ""
  CORS_ORIGINS: str = ""
  S3_ENDPOINT_URL: str = ""
  S3_ACCESS_ID: str = ""
  S3_SECRET_KEY: str = ""
  S3_BUCKETNAME: str = ""
  UPLOAD_FOLDER: str = ""
  MODEL_FOLDER: str = ""
  WEB_BASEPATH: str = "/"
  class Config:
    env_file = ".env" # .env.development .env.production

# settings = Settings()
@lru_cache()
def get_settings():
  return Settings()
