import json
import logging
from typing import Dict

# import jwt
import requests

from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.responses import RedirectResponse

from fastapi import APIRouter
from config import get_settings

OIDC_URL = get_settings().OIDC_URL
OIDC_CLIENT_ID = get_settings().OIDC_CLIENT_ID
OIDC_CALLBACK = get_settings().OIDC_CALLBACK

AUTH_URL = f"{OIDC_URL}/auth?client_id={OIDC_CLIENT_ID}&response_type=code"
TOKEN_URL = f"{OIDC_URL}/token"

router = APIRouter(tags=["oidc"], prefix="/oidc")

## OpenID Connect

@router.get("/login", description="Endpoint for frontend client to call")
async def login() -> RedirectResponse:
  # return { "test": AUTH_URL }
  return RedirectResponse(AUTH_URL)

@router.get("/auth", description="Endpoint for OIDC IDP to callback")
async def auth(code: str) -> RedirectResponse:
  # using grant_type: authorization_code
  payload = f"grant_type=authorization_code&code={code}&redirect_uri={OIDC_CALLBACK}&client_id={OIDC_CLIENT_ID}"
  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  token_response = requests.request("POST", TOKEN_URL, data=payload, headers=headers)

  token_body = json.loads(token_response.content)
  access_token = token_body["access_token"]

  # TBD create own token instead...
  callback_url = f"{OIDC_CALLBACK}#{access_token}" # how about refresh token?
  response = RedirectResponse(url=callback_url)
  response.set_cookie("Authorization", value=f"Bearer {access_token}")
  return response

# @router.get("/")
# async def root(request: Request,) -> Dict:
#   return {"message": "You're logged in! "}
