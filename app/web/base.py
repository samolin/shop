from fastapi import APIRouter
from app.web.auth import route_login
from app.web import home


api_router = APIRouter()
api_router.include_router(route_login.router, prefix="", tags=["auth-web"])
api_router.include_router(home.router, prefix="", tags=["home"])
