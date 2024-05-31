from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin, ModelView

from admin.auth import AdminAuth, authentication_backend
from admin.views import ProductsAdmin, UsersAdmin, CategoriesAdmin
from database import engine
from products.router import router as router_products
from users.router import router as router_users
from core.router import router as router_main


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_products)
app.include_router(router_users)
app.include_router(router_main)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(ProductsAdmin)
admin.add_view(CategoriesAdmin)
