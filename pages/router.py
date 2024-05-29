from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from fastapi_users import FastAPIUsers, fastapi_users

from pydantic import EmailStr
from starlette.templating import _TemplateResponse
from core.models import User
from core.repository import CategoryRepository, ProductRepository
from core.schemas import SProduct, SProductAdd, SProductId, SUserCreate, SUserRead
from core.manager import get_user_manager

from core.security import auth_backend



router = APIRouter(prefix="", tags=["Main"])
templates = Jinja2Templates(directory="templates")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(optional=True)

@router.get("/")
async def get_main_page(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("headings.html", {"request": request, "current_user": user}) 


@router.get("/location")
async def get_location_page(request: Request):
    return templates.TemplateResponse("location.html", {"request": request})


@router.get("/catalog")
async def get_catalog_page(request: Request):
    products = await ProductRepository.find_all()
    categories = await CategoryRepository.find_all()
    return templates.TemplateResponse("catalog.html", {"request": request, "products": products, "categories": categories})


@router.get("/product/{product_id}")
async def get_product_page(request: Request, product_id: int):
    product = await ProductRepository.find_by_id(product_id)
    return templates.TemplateResponse("product.html", {"request": request, "product": product})


@router.get("/products")
async def get_products_category_id(request: Request, category_id: Optional[int] = None):
    products = await ProductRepository.find_all_by_category_id(category_id=category_id)
    category = await CategoryRepository.find_by_id(category_id)
    categories = await CategoryRepository.find_all()
    return templates.TemplateResponse("category.html",
                                      {"request": request, "products": products, "categories": categories,
                                       "category": category})


@router.post("/register")
async def register_user(request: Request,
                        firstname: str = Form(),
                        lastname: str = Form(),
                        patronymic: Optional[str] = Form(None),
                        login: str = Form(),
                        email: EmailStr = Form(),
                        phone: str = Form(),
                        password: str = Form(),
                        password_repeat: str = Form(),
                        UserManager=Depends(get_user_manager)
                        ):
    if password != password_repeat:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    try:
        user = await UserManager.create(user_create=SUserCreate(
            name=firstname,
            surname=lastname,
            patronymic=patronymic,
            login=login,
            email=email,
            phone=phone,
            password=password,
        ))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/register")
async def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/profile")
async def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"
