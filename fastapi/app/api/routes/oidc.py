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
OIDC_CLIENT_SECRET = get_settings().OIDC_CLIENT_SECRET
OIDC_CALLBACK = get_settings().OIDC_CALLBACK

AUTH_URL = f"{OIDC_URL}/auth?"
TOKEN_URL = f"{OIDC_URL}/token"

router = APIRouter(tags=["oidc"], prefix="/oidc")

## OpenID Connect

@router.get("/login", description="Endpoint for frontend client to call")
async def login() -> RedirectResponse:
  payload = f"response_type=code&client_id={OIDC_CLIENT_ID}"
  if (OIDC_CLIENT_SECRET != ""):
    payload = payload + f"&client_secret{OIDC_CLIENT_SECRET}"
  return RedirectResponse(AUTH_URL + payload)

@router.get("/auth", description="Endpoint for OIDC IDP to callback")
async def auth(code: str) -> RedirectResponse:
  # using grant_type: authorization_code
  payload = f"grant_type=authorization_code&code={code}&redirect_uri={OIDC_CALLBACK}&client_id={OIDC_CLIENT_ID}"
  if (OIDC_CLIENT_SECRET != ""):
    payload = payload + f"&client_secret{OIDC_CLIENT_SECRET}"

  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  r = requests.request("POST", TOKEN_URL, data=payload, headers=headers)

  token_body = json.loads(r.content)
  access_token = token_body["access_token"]
  refresh_token = token_body["refresh_token"]

  # TBD create own token instead...
  callback_url = f"{OIDC_CALLBACK}#{access_token}" # how about refresh token?
  response = RedirectResponse(url=callback_url, status_code=302)
  response.set_cookie("Authorization", value=f"Bearer {access_token}", httponly=True)
  response.set_cookie("refresh_token", value=refresh_token, httponly=True)
  return response

@router.get("/refresh", description="Endpoint for OIDC refresh")
async def refresh(refresh_token: str):
  payload = f"grant_type=refresh_token&refresh_token={refresh_token}&client_id={OIDC_CLIENT_ID}"
  if (OIDC_CLIENT_SECRET != ""):
    payload = payload + f"&client_secret{OIDC_CLIENT_SECRET}"

  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  token_response = requests.request("POST", TOKEN_URL, data=payload, headers=headers)

  token_body = json.loads(token_response.content)
  return { "access_token": token_body["access_token"], "refresh_token": token_body["refresh_token"] }
  
# @router.get("/")
# async def root(request: Request,) -> Dict:
#   return {"message": "You're logged in! "}

# this should be moved elsewhere its a common user token verification endpoint
@router.get("/verify", description="Verify user endpoint TBD")
async def verify():
  return "TBD"
