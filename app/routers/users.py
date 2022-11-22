from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.CRUD.users import create_new_user, list_users
from app.db.database import get_db
from app.schemas.users import UserCreate

router = APIRouter()


@router.get("")
def get_users(db: Session = Depends(get_db)):
    users = list_users(db)
    return users


@router.post("/create_new_user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
