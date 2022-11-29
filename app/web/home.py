from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.CRUD.products import list_products
from app.db.database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def base(request: Request, db: Session = Depends(get_db)):
    products = list_products(db)
    [print(prod.img) for prod in products]
    return templates.TemplateResponse(
        "homepage.html", {"request": request, "products": products}
    )

async def get_image_by_name(name):
    with open(f"app/static/prods_img/{name}", "rb") as f:
        f.read()