from sqlalchemy.orm import Session

from ..models.users import User


def list_users(db: Session):
    users = db.query(User).all()
    return users
