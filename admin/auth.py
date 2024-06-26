from fastapi import HTTPException
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from users.auth import authenticate_user, create_access_token
from users.dependencies import get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        login, password = form["username"], form["password"]
        user = await authenticate_user(login, password)
        if user.is_superuser:
            access_token = create_access_token({"sub": str(user.id)})
            request.session.update({"token": access_token})
            return True
        raise HTTPException(status_code=403, detail="Вы не являетесь супер-юзером.")

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> RedirectResponse | bool:
        token = request.session.get("token")
        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        user = await get_current_user(token)
        if not user:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)
        if user.is_superuser:
            return True
        raise HTTPException(status_code=403, detail="Вы не являетесь супер-юзером.")


authentication_backend = AdminAuth(secret_key="...")
