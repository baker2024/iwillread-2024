from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pages.router import router as router_pages
from admin.router import router as router_admin
from core.db_manager import init_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    print("Database tables was created.")
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_pages)
app.include_router(router_admin)






    
