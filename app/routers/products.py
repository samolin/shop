from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.db.CRUD.products import create_new_product, list_products
from app.db.database import get_db
from app.db.models.users import User
from app.routers.login import get_current_user_by_token
from app.schemas.products import ProductCreate

router = APIRouter()


@router.get("")
def get_products(db: Session = Depends(get_db)):
    products = list_products(db)
    return products


@router.post("/product_create")
async def create_product(
    product: ProductCreate = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_by_token),
    file: UploadFile = File(...),
):  
    path = await safe_file_to_uploads(file)
    print(path['filename'])
    product = create_new_product(
        product=product, db=db, current_user=current_user.id, img=path['filename']
    )
    return product

import uuid


async def safe_file_to_uploads(file):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!
    with open(f"app/static/prods_img/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
