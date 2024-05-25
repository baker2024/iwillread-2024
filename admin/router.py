from typing import Annotated
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from core.repository import ProductRepository
from core.schemas import SProduct, SProductAdd, SProductId

router = APIRouter(prefix="/api", tags=["Admin"])
templates = Jinja2Templates(directory="templates")


@router.post("/add/product")
async def add_product(
        product: Annotated[SProductAdd, Depends()],
) -> SProductId:
    product_id = await ProductRepository.add_one(product)
    return {"ok": True, "product_id": product_id}

@router.get("/get/products")
async def get_tasks() -> list[SProduct]:
    products = await ProductRepository.find_all()
    return products