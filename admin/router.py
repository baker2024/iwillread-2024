from typing import Annotated
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates

from sqlalchemy.exc import IntegrityError
from core.repository import CategoryRepository, ProductRepository
from core.schemas import SCategoryAdd, SCategoryId, SProduct, SProductAdd, SProductId

router = APIRouter(prefix="/api", tags=["Admin"])
templates = Jinja2Templates(directory="templates")


@router.post("/add/product")
async def add_product(
        product: Annotated[SProductAdd, Depends()],
) -> SProductId:
    product_id = await ProductRepository.add_one(product)
    if product_id is None:
        raise HTTPException(status_code=400, detail="Category not found")
    return SProductId(ok=True, product_id=product_id)


@router.get("/get/products")
async def get_tasks() -> list[SProduct]:
    products = await ProductRepository.find_all()
    return products


@router.post("/add/category")
async def add_category(
        category: Annotated[SCategoryAdd, Depends()],
) -> SCategoryId:
    try:
        category_id = await CategoryRepository.add_one(category)
        return {"ok": True, "category_id": category_id}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Category already exists")