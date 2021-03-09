from jose import jwt
from fastapi import APIRouter, HTTPException, Depends

from services.auth import auth_user

router = APIRouter(
  prefix="/jwt_test",
  tags=["api-common-jwt_test"],
  # dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

@router.get("/fail")
async def jwt_test_fail():
  try:
    token = jwt.encode({"key": "value"}, "secret", algorithm="HS256")
    decoded = jwt.decode(token, "secret111", algorithms=["HS256"])
  except (jwt.JWTError):
    raise HTTPException(
      status_code=403,
      detail="Could not validate credentials",
    )
  return { "token": token, "decoded": decoded }

@router.get("/")
async def jwt_test():
  token = jwt.encode({"sub": "aaron"}, "secret", algorithm="HS256")
  decoded = jwt.decode(token, "secret", algorithms=["HS256"])
  return { "token": token, "decoded": decoded }

@router.get("/test-middleware")
async def jwt_test_middleware(username = Depends(auth_user)):
  return username