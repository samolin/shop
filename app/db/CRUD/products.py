from sqlalchemy.orm import Session

from app.schemas.products import ProductCreate

from ..models.products import Product


def list_posts(db: Session):
    posts = db.query(Product).all()
    return posts


def create_new_product(product: ProductCreate, db: Session):
    post = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        owner=product.owner,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
