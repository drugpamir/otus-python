from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from homework_04 import config

engine = create_async_engine(
    url=config.DB_CONN_URI,
    echo=config.DB_ECHO,
)

Session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(AsyncAttrs, DeclarativeBase):
    pass
