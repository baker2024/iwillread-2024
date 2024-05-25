from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.repository import ProductRepository
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
    return templates.TemplateResponse("catalog.html", {"request": request, "products": products})


@router.get("/product/{product_id}")
async def get_product_page(request: Request, product_id: int):
    product = await ProductRepository.find_by_id(product_id)
    return templates.TemplateResponse("product.html", {"request": request, "product": product})


@router.get("/register")
async def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})