from fastapi import HTTPException
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from dao.base import BaseDAO
from products.models import Product
from users.models import User
from database import async_session


class UserDAO(BaseDAO):
    model = User

