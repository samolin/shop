from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.base import Base
from app.db.CRUD.users import create_new_user, list_users
from app.db.database import engine, get_db
from app.schemas.users import UserCreate


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
    users = list_users(db)
    return users


@app.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
