from pydantic import BaseSettings
from typing import Optional
import logging
from functools import lru_cache # read .env only once

logger = logging.getLogger(__name__)
logger.warn("Logging @ %s", __name__)

import random
import string

class CommonSettings(BaseSettings):
  ENV: str = "undefined"
  APP: str = "custom_app"
  VERSION: str = "0.0.0"
  class Config:
    env_file = ".env"

class EnvSettings(BaseSettings):
  ENV: str = CommonSettings().ENV
  APP: str = CommonSettings().APP
  VERSION: str = CommonSettings().VERSION
  JWT_ALG: str = "HS256"
  JWT_SECRET: str = "".join(random.choice(string.ascii_letters) for i in range(32))
  REFRESH_TOKEN_SECRET: str = "".join(random.choice(string.ascii_letters) for i in range(64))
  JWT_EXPIRY_S: int = 300
  REFRESH_TOKEN_EXPIRY_S: int = 3600
  API_PORT: int = 3000
  SQLALCHEMY_DB_URL: Optional[str] = "" # to be made a list
  CORS_ORIGINS: str = ""
  S3_ENDPOINT_URL: str = ""
  S3_ACCESS_ID: str = ""
  S3_SECRET_KEY: str = ""
  S3_BUCKETNAME: str = ""
  UPLOAD_FOLDER: str = ""
  MODEL_FOLDER: str = ""
  WEB_BASEPATH: str = "/"
  REDIS_CONNECTION: str = ""
  HUEY_REDIS_CONNECTION: str = ""
  HUEY_TASK_QUEUES: str = "" # to be made a list

  MONGODB_URL: str = "" # to be made a list
  MONGODB_DB: str = "" # to be made a list

  USE_HTTPS: int = 0
  HTTPS_CERT_PATH: str = ""
  HTTPS_KEY_PATH: str = ""

  OIDC_URL: str = ""
  OIDC_CLIENT_ID: str = ""
  OIDC_CLIENT_SECRET: str = ""
  OIDC_CALLBACK: str = ""

  OAUTH_URL: str = ""
  OAUTH_CLIENT_ID: str = ""
  OAUTH_CLIENT_SECRET: str = ""
  OAUTH_CALLBACK: str = ""
  OAUTH_USER_URL: str = ""
  OAUTH_USER_ID: str = ""
  OAUTH_USER_GROUPS: str = "" # unused
  OAUTH_FIND_ID: str = "" # unused

  SAML_SETTINGS_FILEPATH: str = ""
  SAML_CALLBACK: str = ""

  class Config:
    env_file = ".env." + CommonSettings().ENV # .env.development .env.production

# settings = Settings()
@lru_cache()
def get_settings():
  return EnvSettings()
