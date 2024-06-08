from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_HOST = "postgres://baker:MEg2U5wcih9AjCseeIpiJ9JNBByAFsYU@dpg-cpi133i1hbls73bad6r0-a.frankfurt-postgres.render.com/iwillsew_database"
DB_PORT = 5432
DB_USER = "baker"
DB_PASSWORD = "MEg2U5wcih9AjCseeIpiJ9JNBByAFsYU"
DB_DATABASE = "iwillsew_database"


DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
)
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
