from fastapi import HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader

from jose import jwt
from typing import Optional
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
apiKeyHeader_scheme = APIKeyHeader(name="Authorization")

from config import get_settings

# oauth2_scheme, apiKeyHeader_scheme
async def auth_user(token: str = Depends(apiKeyHeader_scheme)):
  credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    decoded = jwt.decode(token, get_settings().JWT_SECRET, algorithms=["HS256"])
    # username = decoded.get("sub")
    # if username is None:
    #     raise credentials_exception
    # token_data = TokenData(username=username)
  except jwt.JWTError:
    raise credentials_exception
  return decoded

async def decode_token(tokens):
  decoded = jwt.decode(tokens["access_token"], get_settings().JWT_SECRET, algorithms=["HS256"])
  return decoded

# create access_token and refresh_token
async def create_token(
  payload: dict,
  access_token_exp_timedelta: Optional[timedelta] = None,
  refresh_token_exp_timedelta: Optional[timedelta] = None
):
  # try:
  #     items = any_object.items()
  # except (AttributeError, TypeError):
  #     non_items_behavior(any_object)
  # else: # no exception raised
  #     for item in items: ...
  access_payload = payload.copy() # should contain user id, user groups and expiry
  expire = datetime.utcnow() + timedelta(minutes=15)
  if access_token_exp_timedelta:
    expire = datetime.utcnow() + access_token_exp_timedelta
  access_payload.update({"exp": expire}) # add expiry

  refresh_payload = payload.copy() # should just contain user id and expiry
  expire = datetime.utcnow() + timedelta(days=1)
  if refresh_token_exp_timedelta:
    expire = datetime.utcnow() + refresh_token_exp_timedelta
  refresh_payload = { "exp": expire, **refresh_payload } # another way to add expiry

  access_token = jwt.encode(access_payload, get_settings().JWT_SECRET, algorithm="HS256")
  refresh_token = jwt.encode(refresh_payload, get_settings().REFRESH_TOKEN_SECRET, algorithm="HS256")

  # payload_dict = payload.dict()
  # new_payload = { "new_property": "new_data", **payload.dict() }
  # token = jwt.encode(jsonable_encoder(payload_dict), get_settings().JWT_SECRET, algorithm="HS256")
  return { "access_token": access_token, "refresh_token": refresh_token }
