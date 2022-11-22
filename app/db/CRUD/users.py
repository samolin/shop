from sqlalchemy.orm import Session

from app.core.hashing import Hasher
from app.schemas.users import UserCreate

from ..models.users import User


def list_users(db: Session):
    users = db.query(User).all()
    return users


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
