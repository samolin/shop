from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.CRUD.categories import create_new_category
from app.db.database import get_db
from app.db.models.users import User
from app.routers.login import get_current_user_by_token
from app.schemas.categories import CategoryCreate

router = APIRouter()


@router.post("/category_create")
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_by_token),
):
    category = create_new_category(category=category, db=db)
    return category
