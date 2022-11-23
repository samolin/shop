from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.CRUD.users import create_new_user, list_users
from app.db.database import get_db
from app.routers.login import get_current_user_by_token
from app.schemas.users import User, UserCreate

router = APIRouter()


@router.get("")
def get_users(db: Session = Depends(get_db)):
    users = list_users(db)
    return users


@router.post("/create_new_user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.post("/me")
def show_me(current_user: User = Depends(get_current_user_by_token)):
    return current_user
