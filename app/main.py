from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import get_db, engine
from app.db.CRUD.users import list_users
from app.db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION
    )
    create_tables()
    return app


app = start_application()


@app.get("/")
def test(db: Session = Depends(get_db)):
    jobs = list_users(db)
    return jobs
