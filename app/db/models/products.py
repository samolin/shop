from sqlalchemy import Column, ForeignKey, Integer, String

from ..base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(Integer, ForeignKey("category.id"), nullable=False)
    owner = Column(Integer, ForeignKey("user.id"), nullable=False)
