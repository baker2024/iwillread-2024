import json
from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from products.dao import ProductDAO
from products.models import Author, Product
from users.dependencies import get_current_user
from users.models import User

router = APIRouter(prefix="", tags=["Products"])
templates = Jinja2Templates(directory="templates")


@router.get("/catalog")
async def get_catalog_page(request: Request, user: User = Depends(get_current_user)):
    products = await ProductDAO.find_all_with_images()
    categories = await ProductDAO.find_all_categories()
    return templates.TemplateResponse(
        "catalog.html",
        {
            "request": request,
            "products": products,
            "categories": categories,
            "user": user,
        },
    )


@router.get("/products")
async def get_products(
    request: Request,
    category_id: int = Query(None),
    sort_by: str = Query(None),
    user: User = Depends(get_current_user),
):
    products = await ProductDAO.find_all_filter(category_id, sort_by)
    categories = await ProductDAO.find_all_categories()
    return templates.TemplateResponse(
        "catalog.html",
        {
            "request": request,
            "products": products,
            "categories": categories,
            "user": user,
        },
    )


@router.get("/get-products")
async def get_products_filter(
    category_id: int = Query(None),
    sort_by: str = Query(None),
):
    products = await ProductDAO.find_all_filter(category_id, sort_by)
    serialized_products = [dict(product) for product in products]
    return {"products": serialized_products}


@router.get("/product")
async def get_product_page(
    request: Request, product_id: int, user: User = Depends(get_current_user)
):
    product = await ProductDAO.find_product_by_id(product_id)
    author = await ProductDAO.find_author_by_id(product.author_id)
    return templates.TemplateResponse(
        "product.html",
        {"request": request, "product": product, "user": user, "author": author},
    )


@router.get("/author")
async def get_author(
    request: Request, id: int = Query(None), user: User = Depends(get_current_user)
):
    if id:
        products = await ProductDAO.find_all_filter(id)
        author = await ProductDAO.find_author_by_id(id)
        serialized_products = [dict(product) for product in products]
        return templates.TemplateResponse(
            "author.html",
            {
                "request": request,
                "products": serialized_products,
                "author": author,
                "user": user,
            },
        )


@router.get("/authors")
async def get_authors(request: Request, user: User = Depends(get_current_user)):
    authors = await ProductDAO.find_all_authors()
    return templates.TemplateResponse(
        "authors.html",
        {
            "request": request,
            "authors": authors,
            "user": user,
        },
    )


@router.get("/search")
async def search_books_and_authors(
    request: Request, user: User = Depends(get_current_user)
):
    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "user": user,
        },
    )


@router.get("/find-data")
async def find_data(
    request: Request, query: str = Query(...), user: User = Depends(get_current_user)
):
    results = await ProductDAO.search(query=query)
    books = []
    authors = []
    for result in results:
        if isinstance(result, Author):
            authors.append(result)
        elif isinstance(result, Product):
            books.append(result)
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "books": books,
            "authors": authors,
            "user": user,
        },
    )
