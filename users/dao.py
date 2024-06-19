from fastapi import HTTPException
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from dao.base import BaseDAO
from products.models import Product
from users.models import User
from database import async_session


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def check_superuser(cls, user_login):
        async with async_session() as session:
            async with session.begin():
                query = select(User).where(
                    User.login == user_login, User.is_superuser.is_(True)
                )
                result = await session.execute(query)
                return result.scalar() is not None
