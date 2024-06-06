from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

from products.dao import ProductDAO
from products.models import Product
from users.dependencies import get_current_user
from users.models import User

router = APIRouter(prefix="", tags=["Main"])
templates = Jinja2Templates(directory="templates")


@router.get("/register")
async def get_register_page(request: Request, user: User = Depends(get_current_user)):
    if user:
        return RedirectResponse("/me")
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login")
async def get_login_page(request: Request, user: User = Depends(get_current_user)):
    if user:
        return RedirectResponse("/me")
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/location")
async def get_location_page(request: Request, user: User = Depends(get_current_user)):
    return templates.TemplateResponse("location.html", {"request": request, "user": user})


@router.get("/me")
async def user_profile(request: Request, user: User = Depends(get_current_user)):
    if not user:
        return RedirectResponse("/login")
    return templates.TemplateResponse("me.html", {"request": request, "user": user})


@router.get("/")
async def get_about_page(request: Request, user: User = Depends(get_current_user)):
    latests_products = await ProductDAO.find_latests_five()
    return templates.TemplateResponse("about_us.html", {"request": request, "user": user, "products": latests_products})
