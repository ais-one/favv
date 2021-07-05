from fastapi import APIRouter, Response, Depends, Request
from api.routes.auth.jwt import router as router_jwt
from services.auth import do_refresh_token, auth_user, create_token, test_auth

router = APIRouter(prefix="/auth")

router.include_router(router_jwt)

# verify user
@router.get("/test", tags=["api_auth"])
async def test(decoded = Depends(test_auth)):
  return decoded

# verify user
@router.get("/verify", tags=["api_auth"])
async def verify(decoded = Depends(auth_user)):
  return decoded

# decoded = Depends(do_refresh_token)
@router.post("/refresh", tags=["api_auth"])
async def refresh(tokens = Depends(do_refresh_token)):
  # response.status_code = 201 # change status code
  return {
    "access_token": tokens["access_token"],
    "refresh_token": tokens["refresh_token"],
  }

# Cookie
# ads_id: Optional[str] = Cookie(None)
