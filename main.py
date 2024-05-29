from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers, fastapi_users

from core.manager import get_user_manager
from core.models import User
from core.schemas import SUserCreate, SUserRead
from pages.router import router as router_pages
from admin.router import router as router_admin
from core.db_manager import init_models
from core.security import auth_backend


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    print("Database tables was created.")
    yield


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_pages)
app.include_router(router_admin)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(SUserRead, SUserCreate),
    prefix="/auth",
    tags=["auth"],
)





    
