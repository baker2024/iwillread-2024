from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from exceptions import UserAlreadyExistsException
from users.auth import get_password_hash, authenticate_user, create_access_token
from users.dao import UserDAO
from users.dependencies import get_current_user
from users.models import User
from users.schemas import SUserAuth, SUserCreate

router = APIRouter(prefix="/auth", tags=["Auth"])
templates = Jinja2Templates(directory="templates")


@router.post("/register", status_code=201)
async def register_user(user_data: SUserCreate):
    existing_user_email = await UserDAO.find_one_or_none(email=user_data.email)
    existing_user_login = await UserDAO.find_one_or_none(login=user_data.login)
    existing_user_phone = await UserDAO.find_one_or_none(phone=user_data.phone)

    existing_users = {
        "Email": existing_user_email,
        "Логин": existing_user_login,
        "Номер телефона": existing_user_phone
    }

    for field, existing_user in existing_users.items():
        if existing_user:
            raise HTTPException(409, detail=f"Пользователь уже существует с таким же: {field}")

    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(name=user_data.name,
                      surname=user_data.surname,
                      patronymic=user_data.patronymic,
                      login=user_data.login,
                      phone=user_data.phone,
                      email=user_data.email,
                      hashed_password=hashed_password)
    return {"ok": True}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.login, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")



