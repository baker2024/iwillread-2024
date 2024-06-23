from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_HOST = "dpg-cps6auqj1k6c738igfk0-a.frankfurt-postgres.render.com/iwillread"
DB_PORT = 5432
DB_USER = "baker"
DB_PASSWORD = "UksBaJ5UH2pwL2bi9zfhVAiWoYkJkBom"
DB_DATABASE = "iwillread"


DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
)
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
