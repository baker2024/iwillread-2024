from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin, ModelView

from fastapi.middleware.cors import CORSMiddleware
from admin.auth import AdminAuth, authentication_backend
from admin.views import ProductsAdmin, UsersAdmin, CategoriesAdmin, OrdersAdmin
from database import engine
from products.router import router as router_products
from users.router import router as router_users
from core.router import router as router_main
from basket.router import router as router_basket
from orders.router import router as router_orders

print("hello world")


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    # 3000 - порт, на котором работает фронтенд на React.js
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://iwillsew.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


app.include_router(router_products)
app.include_router(router_users)
app.include_router(router_main)
app.include_router(router_basket)
app.include_router(router_orders)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(ProductsAdmin)
admin.add_view(CategoriesAdmin)
admin.add_view(OrdersAdmin)
