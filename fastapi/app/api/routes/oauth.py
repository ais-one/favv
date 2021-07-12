# replaces fastapi-sso

import json
import logging
from typing import Dict, Optional
import requests

# from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi import APIRouter

from config import get_settings
from services.auth import create_token

OAUTH_URL = get_settings().OAUTH_URL
OAUTH_CLIENT_ID = get_settings().OAUTH_CLIENT_ID
OAUTH_CLIENT_SECRET = get_settings().OAUTH_CLIENT_SECRET
OAUTH_CALLBACK = get_settings().OAUTH_CALLBACK
OAUTH_USER_URL = get_settings().OAUTH_USER_URL
OAUTH_USER_ID = get_settings().OAUTH_USER_ID

router = APIRouter(tags=["oauth"], prefix="/oauth")

## OAuth

@router.get("/callback", description="Endpoint for OAuth to callback")
async def auth(code: str, state: Optional[str] = None) -> RedirectResponse:
  try:
    headers = {'Accept': 'application/json'}
    payload = {
      "client_id": OAUTH_CLIENT_ID,
      "client_secret": OAUTH_CLIENT_SECRET,
      "code": code
    }
    if state:
      payload["state"] = state
    r = requests.post(OAUTH_URL, json=payload, headers=headers)
    body = json.loads(r.content)

    headers = {'Authorization': 'token ' + body["access_token"]}
    r = requests.get(OAUTH_USER_URL, headers=headers)
    body = json.loads(r.content)
    # print(body)

    # return "TBD1"
    id = body[OAUTH_USER_ID]
    groups = []
    tokens = await create_token({ "id": id, "groups": groups })
    access_token = tokens["access_token"]
    refresh_token = tokens["refresh_token"]
    callback_url = f"{OAUTH_CALLBACK}#{access_token}-{refresh_token}-"
    response = RedirectResponse(url=callback_url, status_code=302)
    response.set_cookie("Authorization", value=f"Bearer {access_token}", httponly=True)
    response.set_cookie("refresh_token", value=refresh_token, httponly=True)
    return response
  except Exception as e:
    print(e)
    return "Error"