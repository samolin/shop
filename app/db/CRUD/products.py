from sqlalchemy.orm import Session

from app.schemas.products import ProductCreate

from ..models.products import Product


def list_products(db: Session):
    products = db.query(Product).all()
    return products


def create_new_product(product: ProductCreate, db: Session, current_user: int, img: str):
    product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        owner=current_user,
        img=img
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
