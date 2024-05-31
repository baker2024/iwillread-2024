from typing import Optional

from pydantic import BaseModel, EmailStr


class SUserCreate(BaseModel):
    name: str
    surname: str
    patronymic: Optional[str]
    login: str
    email: EmailStr
    phone: str
    password: str


class SUserAuth(BaseModel):
    login: str
    password: str
