# https://python-jose.readthedocs.io/en/latest/

from fastapi import HTTPException, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from fastapi.responses import JSONResponse

from jose import jwt
from typing import Optional
from datetime import datetime, timedelta

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
apiKeyHeader_scheme = APIKeyHeader(name="Authorization") # Authorization: Bearer XXXXX

from config import get_settings

async def test_auth(request: Request):
  # request.headers['some-header']
  # request.cookies.get('mycookie')
  # print(request.query_params['a-param'])
  return "extract request stuff"

# oauth2_scheme, apiKeyHeader_scheme
async def auth_user(access_token: str = Depends(apiKeyHeader_scheme)):
  credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    decoded = jwt.decode(access_token, get_settings().JWT_SECRET, algorithms=["HS256"])
    # username = decoded.get("sub")
    # if username is None:
    #     raise credentials_exception
    # token_data = TokenData(username=username)
    return decoded
  except jwt.ExpiredSignatureError:
    return JSONResponse( status_code=401, content={"message": "Token Expired Error"} )
  except jwt.JWTError:
    return JSONResponse( status_code=400, content={"message": "Token Error"} )

async def do_refresh_token(refresh_token: str = Depends(apiKeyHeader_scheme)):
  try:
    refresh_token = refresh_token.split(" ")[1]
    decoded = jwt.decode(refresh_token, get_settings().REFRESH_TOKEN_SECRET, algorithms=["HS256"])
    return await create_token(decoded)
  except jwt.JWTError as e:
    print(e)
    return None
    
async def decode_token(tokens):
  decoded = jwt.decode(tokens["access_token"], get_settings().JWT_SECRET, algorithms=["HS256"])
  return decoded

# create access_token and refresh_token
async def create_token(payload: dict):
  # try:
  #     items = any_object.items()
  # except (AttributeError, TypeError):
  #     non_items_behavior(any_object)
  # else: # no exception raised
  #     for item in items: ...
  try:
    now = datetime.utcnow()

    access_payload = payload.copy() # should contain user id, user groups and expiry
    access_payload.update({ "exp": now + timedelta(seconds=get_settings().JWT_EXPIRY_S) }) # add expiry

    refresh_payload = payload.copy() # should just contain user id and expiry
    refresh_payload = { **refresh_payload, "exp": now + timedelta(seconds=get_settings().REFRESH_TOKEN_EXPIRY_S) } # another way to add expiry

    access_token = jwt.encode(access_payload, get_settings().JWT_SECRET, algorithm="HS256")
    refresh_token = jwt.encode(refresh_payload, get_settings().REFRESH_TOKEN_SECRET, algorithm="HS256")

    # payload_dict = payload.dict()
    # new_payload = { "new_property": "new_data", **payload.dict() }
    # token = jwt.encode(jsonable_encoder(payload_dict), get_settings().JWT_SECRET, algorithm="HS256")
    return { "access_token": access_token, "refresh_token": refresh_token }
  except:
    # raise HTTPException(status_code=401, detail="Create token error")
    return None
