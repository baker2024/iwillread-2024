from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from products.dao import ProductDAO

router = APIRouter(prefix="", tags=["Products"])
templates = Jinja2Templates(directory="templates")


@router.get("/catalog")
async def get_catalog_page(request: Request):
    products = await ProductDAO.find_all_with_images()
    categories = await ProductDAO.find_all_categories()
    return templates.TemplateResponse("catalog.html", {"request": request,
                                                       "products": products,
                                                       "categories": categories})


@router.get("/products")
async def get_products(request: Request, category_id: int):
    category_products = await ProductDAO.find_all_by_category(category_id)
    categories = await ProductDAO.find_all_categories()
    category = await ProductDAO.find_category_by_id(category_id)
    print(category)
    return templates.TemplateResponse("category.html", {"request": request,
                                                        "products": category_products,
                                                        "categories": categories,
                                                        "category": category})


@router.get("/product")
async def get_product_page(request: Request, product_id: int):
    product = await ProductDAO.find_product_by_id(product_id)
    return templates.TemplateResponse("product.html", {"request": request,
                                                       "product": product})


