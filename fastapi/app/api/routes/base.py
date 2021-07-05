from fastapi import APIRouter, Response

from api.routes.test import router as router_test # or... from .test
from api.routes.oidc import router as router_oidc
from api.routes.oauth import router as router_oauth
from api.routes.saml import router as router_saml
from api.routes.auth.base import router as router_auth

from config import get_settings

import importlib
import os
import sys

app_env = get_settings().ENV

router_app = None # dynamically import route
app_name = get_settings().APP
# router_app = getattr(importlib.import_module("api.routes." + app_name + ".base"), "router_" + app_name)
lib_path = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
sys.path.append(lib_path)
router_app = getattr(importlib.import_module(app_name + ".base"), "router_" + app_name)

router = APIRouter()

router.include_router(router_auth)
router.include_router(router_oidc)
router.include_router(router_saml)
router.include_router(router_oauth)
if app_env != "production":
  router.include_router(router_test)
if router_app:
  router.include_router(router_app)


@router.get("/healthcheck",
#   status_code=200, # add status code
#   summary="openapi summary",
#   description="openapi description",
#   response_description="a response description"
#   # deprecated=True # indicate deprecated
#   # response_model=Item
)
async def healthcheck():
  return {
    "Endpoint": "GET /api/healthcheck",
    "App": get_settings().APP,
    "Version": get_settings().VERSION
  }

@router.post("/healthcheck")
async def healthcheck_post(response: Response):
  response.status_code = 201 # change status code
  return {
    "Endpoint": "POST /api/healthcheck",
    "App": get_settings().APP,
    "Version": get_settings().VERSION
  }
