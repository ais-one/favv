from fastapi import APIRouter
from api.routes.common.jwt import router as router_jwt

router = APIRouter(
  prefix="/common",
)

router.include_router(router_jwt)
