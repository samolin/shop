from sqlalchemy import Integer, String, Column

from ..base_class import Base


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
