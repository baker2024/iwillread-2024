from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = getenv("DATABASE_URL")
    db_name: str = getenv("DATABASE_NAME")
    db_user: str = getenv("DATABASE_USER")
    db_password: str = getenv("DATABASE_PASSWORD")
    db_port: int = getenv("DATABASE_PORT")
    db_host: str = getenv("DATABASE_HOST")


settings = Settings()
