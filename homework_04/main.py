"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import logging

from jsonplaceholder_requests import get_users_from_service, get_posts_from_service
from models import crud, engine, Session, Base
import common

log = logging.getLogger(__name__)


async def async_main():
    log.info("Create database")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    log.info("Load data from http")
    users, posts = await asyncio.gather(
        get_users_from_service(),
        get_posts_from_service(),
    )

    log.info("Write to database")
    async with Session() as session:
        await crud.create_users(session, users)
        await crud.create_posts(session, posts)

    log.info("Main is done")


def main():
    common.configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
