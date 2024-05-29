from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi_users import schemas


class SProductAdd(BaseModel):
    name: str
    description: Optional[str]
    price: int
    count: int
    category_id: int

class SProduct(SProductAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SProductId(BaseModel):
    ok: bool = True
    product_id: int


class SCategoryAdd(BaseModel):
    name: str

class SCategory(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class SCategoryId(BaseModel):
    ok: bool = True
    category_id: int


class SUserRead(schemas.BaseUser[int]):
    id: int
    name: str
    surname: str
    patronymic: Optional[str]
    login: str
    email: EmailStr
    phone: str

    model_config = ConfigDict(from_attributes=True)


class SUserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    patronymic: Optional[str]
    login: str
    email: EmailStr
    phone: str



class SUserUpdate(schemas.BaseUserUpdate):
    pass
