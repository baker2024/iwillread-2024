from fastapi import Depends, Request
from jose import ExpiredSignatureError, JWTError, jwt

from core import config
from exceptions import UserIsNotPresentException
from users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return False
    return token


async def get_current_user(token: str = Depends(get_token)):
    if token:
        try:
            payload = jwt.decode(token, config.SECRET_KEY, config.ALGORITHM)
        except ExpiredSignatureError:
            return False
        except JWTError:
            return False
        user_id: str = payload.get("sub")
        if not user_id:
            raise UserIsNotPresentException
        user = await UserDAO.find_one_or_none(id=int(user_id))
        if not user:
            raise UserIsNotPresentException
    else:
        return False

    return user
