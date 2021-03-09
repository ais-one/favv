from jose import jwt
from fastapi import APIRouter, HTTPException, Depends

from config import get_settings
from services.auth import auth_user, create_token

router = APIRouter(
  prefix="/jwt-test",
  tags=["api_common_jwt-test"],
  # dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

@router.get("/fail")
async def jwt_test_fail():
  try:
    tokens = create_token({ "key": "value" })
    decoded = jwt.decode(tokens["access_token"], "secret111", algorithms=["HS256"])
  except (jwt.JWTError):
    raise HTTPException(
      status_code=403,
      detail="Could not validate credentials",
    )
  return { "token": token, "decoded": decoded }

@router.get("/")
async def jwt_test():
  tokens = await create_token({ "key": "value" })
  decoded = jwt.decode(tokens["access_token"], get_settings().JWT_SECRET, algorithms=["HS256"])
  return { "tokens": tokens, "decoded": decoded }

@router.get("/test-middleware")
async def jwt_test_middleware(decoded = Depends(auth_user)):
  return decoded