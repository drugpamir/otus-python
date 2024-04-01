from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Post


async def create_users(session: AsyncSession, users: List[User]):
    session.add_all(users)
    await session.commit()


async def create_posts(session: AsyncSession, posts: List[Post]):
    session.add_all(posts)
    await session.commit()

