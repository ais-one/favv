import json
import logging
from typing import Dict

# import jwt
import requests

from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.responses import RedirectResponse

from fastapi import APIRouter

APP_BASE_URL = "http://127.0.0.1:8000/api/custom-app/oidc/"
KEYCLOAK_BASE_URL = "http://127.0.0.1:8081"
CLIENT_ID = "test-oidc-client-favv"
REALM = "test"

AUTH_URL = (
  f"{KEYCLOAK_BASE_URL}/auth/realms/{REALM}/protocol/openid-connect/auth?client_id={CLIENT_ID}&response_type=code"
)
TOKEN_URL = (
  f"{KEYCLOAK_BASE_URL}/auth/realms/{REALM}/protocol/openid-connect/token"
)

router_custom_app_oidc = APIRouter(tags=["custom_app_oidc"], prefix="/oidc")

## OpenID Connect

@router_custom_app_oidc.get("/login")
async def login() -> RedirectResponse:
  # return { "test": AUTH_URL }
  return RedirectResponse(AUTH_URL)


@router_custom_app_oidc.get("/auth")
async def auth(code: str) -> RedirectResponse:
  payload = (
    f"grant_type=authorization_code&code={code}&redirect_uri={APP_BASE_URL}&client_id={CLIENT_ID}"
  )
  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  token_response = requests.request(
    "POST", TOKEN_URL, data=payload, headers=headers
  )

  token_body = json.loads(token_response.content)
  access_token = token_body["access_token"]

  response = RedirectResponse(url="/api/custom-app/oidc/")
  response.set_cookie("Authorization", value=f"Bearer {access_token}")
  return response
  # return { "test": "OK" }


@router_custom_app_oidc.get("/")
async def root(request: Request,) -> Dict:
  authorization: str = request.cookies.get("Authorization")
  scheme, credentials = get_authorization_scheme_param(authorization)
  # decoded = jwt.decode(
  #   credentials, verify=False
  # ) # TODO input keycloak public key as key, disable option to verify aud
  print("credentials")
  return {"message": "You're logged in! "}
