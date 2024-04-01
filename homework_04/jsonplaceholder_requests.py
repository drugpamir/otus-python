"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from aiohttp import ClientSession
import logging
from typing import List

from models import User, Post

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

log = logging.getLogger(__name__)


async def fetch_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_users_from_service() -> List[User]:
    log.info('Try to get users by URL')

    list_jsons: List[dict] = await fetch_api(USERS_DATA_URL)

    users_out = [
        User.from_json_user_in(j)
        for j in list_jsons
    ]

    log.info('Got users by URL')

    return users_out


async def get_posts_from_service() -> List[Post]:
    log.info('Try to get posts by URL')

    list_jsons: List[dict] = await fetch_api(POSTS_DATA_URL)

    posts_out = [
        Post.from_json_post_in(j)
        for j in list_jsons
    ]

    log.info('Got posts by URL')

    return posts_out
