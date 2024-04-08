from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="", tags=["Main"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_main_page(request: Request):
    return templates.TemplateResponse("headings.html", {"request": request})


@router.get("/location")
async def get_location_page(request: Request):
    return templates.TemplateResponse("location.html", {"request": request})\
    

@router.get("/catalog")
async def get_catalog_page(request: Request):
    return templates.TemplateResponse("catalog.html", {"request": request})

@router.get("/register")
async def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})