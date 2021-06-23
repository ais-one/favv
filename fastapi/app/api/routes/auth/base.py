from fastapi import APIRouter
from api.routes.auth.jwt import router as router_jwt

router = APIRouter(prefix="/auth")

router.include_router(router_jwt)
