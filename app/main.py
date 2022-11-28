from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app.routers.base import api_router
from app.web.base import api_router as web_api_router
from fastapi.staticfiles import StaticFiles


def include_router(app):
    app.include_router(api_router)
    app.include_router(web_api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION
    )
    create_tables()
    include_router(app)
    configure_static(app)
    return app


app = start_application()
