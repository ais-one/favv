import json
import logging
from typing import Dict

# import jwt
import requests

# from starlette.requests import Request
from starlette.responses import RedirectResponse

from fastapi import APIRouter
from config import get_settings

OAUTH_URL = get_settings().OAUTH_URL
OAUTH_CLIENT_ID = get_settings().OAUTH_CLIENT_ID
OAUTH_CLIENT_SECRET = get_settings().OAUTH_CLIENT_SECRET
OAUTH_CALLBACK = get_settings().OAUTH_CALLBACK

router = APIRouter(tags=["oauth"], prefix="/oauth")

## OAuth

@router.get("/auth", description="Endpoint for OAuth to callback")
async def auth(code: str, state: str) -> RedirectResponse:
  payload = {
    "client_id": OAUTH_CLIENT_ID,
    "client_secret": OAUTH_CLIENT_SECRET,
    "code": code,
    "state": state
  }
  r = requests.post(OAUTH_URL, json=payload)

  # token_body = json.loads(token_response.content)
  # access_token = token_body["access_token"]

  # TBD create own token instead...
  # return res.redirect(OAUTH_CALLBACK + '#' + tokens.access_token + '-' + tokens.refresh_token + '-' + JSON.stringify(tokens.user_meta)) // use url fragment...
  callback_url = f"{OAUTH_CALLBACK}#{access_token}" # how about refresh token?
  response = RedirectResponse(url=callback_url)
  response.set_cookie("Authorization", value=f"Bearer {access_token}")
  return response
