from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    category: str
