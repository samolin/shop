from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.CRUD.products import create_new_product, list_posts
from app.db.database import get_db
from app.schemas.products import ProductCreate

router = APIRouter()


@router.get("")
def get_products(db: Session = Depends(get_db)):
    products = list_posts(db)
    return products


@router.post("/product_create")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = create_new_product(product=product, db=db)
    return product
