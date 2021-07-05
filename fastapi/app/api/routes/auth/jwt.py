from jose import jwt
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from config import get_settings
from services.auth import auth_user, create_token

router = APIRouter(
  prefix="/jwt-test",
  tags=["api_jwt-test"],
  # dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

@router.get("/fail")
async def jwt_test_fail():
  try:
    tokens = await create_token({ "key": "value" })
    decoded = jwt.decode(tokens["access_token"], "secret111", algorithms=["HS256"])
  except jwt.JWTError:
    raise HTTPException( status_code=403, detail="Could not validate credentials" )
    # return JSONResponse( status_code=418, content={"message": "Force Failure"} )
  return { "access_token": tokens["access_token"], "decoded": decoded }

@router.get("/")
async def jwt_test():
  tokens = await create_token({ "key": "value" })
  decoded = jwt.decode(tokens["access_token"], get_settings().JWT_SECRET, algorithms=["HS256"])
  return { "tokens": tokens, "decoded": decoded }

@router.get("/test-middleware")
async def jwt_test_middleware(decoded = Depends(auth_user)):
  return decoded

# response.set_cookie(oauth2_scheme.token_name, encoded_jwt, httponly=True)
@router.get("/fake-login")
async def fake_login():
  tokens = await create_token({ "key": "value" })
  res = JSONResponse(tokens)
  res.status_code = 200
  # res.set_cookie(, encoded_jwt, httponly=True)
  return res
