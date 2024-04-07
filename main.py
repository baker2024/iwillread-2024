import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pages.router import router as router_pages

app = FastAPI()
app.include_router(router_pages)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/admin")
async def admin_panel():
    return {"message": "Admin Panel"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
