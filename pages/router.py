from typing import Optional
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.repository import CategoryRepository, ProductRepository
from core.schemas import SProduct, SProductAdd, SProductId


router = APIRouter(prefix="", tags=["Main"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_main_page(request: Request):
    return templates.TemplateResponse("headings.html", {"request": request})


@router.get("/location")
async def get_location_page(request: Request):
    return templates.TemplateResponse("location.html", {"request": request})
    

@router.get("/catalog")
async def get_catalog_page(request: Request):
    products = await ProductRepository.find_all()
    categories = await CategoryRepository.find_all()
    return templates.TemplateResponse("catalog.html", {"request": request, "products": products, "categories": categories})


@router.get("/product/{product_id}")
async def get_product_page(request: Request, product_id: int) -> SProduct:
    product = await ProductRepository.find_by_id(product_id)
    return templates.TemplateResponse("product.html", {"request": request, "product": product})


@router.get("/products")
async def get_products_category_id(request: Request, category_id: Optional[int] = None):
    products = await ProductRepository.find_all_by_category_id(category_id=category_id)
    category = await CategoryRepository.find_by_id(category_id)
    categories = await CategoryRepository.find_all()
    return templates.TemplateResponse("category.html", {"request": request, "products": products, "categories": categories, "category": category})


@router.get("/register")
async def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})