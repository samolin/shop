from sqlalchemy.orm import Session

from app.schemas.categories import CategoryCreate

from ..models.categories import Category


def create_new_category(category: CategoryCreate, db: Session):
    category = Category(
        name = category.name,
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
