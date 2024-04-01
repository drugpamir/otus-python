from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from . import User, Post


# async def create_user(session: AsyncSession, username: str, email: str, name: str, is_stuff: bool = False) -> User:
#     user = User(username, email, name, is_stuff)
#     await create_users(session, user)
#     print("Created:", user)
#     return user


async def create_users(session: AsyncSession, users: List[User]):
    session.add_all(users)
    await session.commit()


# async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
#     user = await session.get(User, user_id)
#     print(f"Found by id {user_id}: {user}")
#     return user
#
#
# async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
#     user = await session.query(User).filter_by(username=username).one_or_none()
#     print(f"Found by username {username}: {user}")
#     return user
#
#
# async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
#     user = await session.query(User).filter(User.email == email).one_or_none()
#     print(f"Found by email {email}: {user}")
#     return user
#
#
# async def get_user_by_email_domain(session: AsyncSession, domain: str) -> list[User]:
#     users = await session.query(User).filter(User.email.ilike(f"%{domain}")).order_by(User.id).all()
#     print(f"Found by domain {domain}: {users}")
#     return users
#
#
# async def get_users(session: AsyncSession) -> list[User]:
#     users = await session.query(User).order_by(User.id).all()
#     print("List of Users:", users)
#     return users


# async def create_post(session: AsyncSession, username: str, email: str, name: str, is_stuff: bool = False) -> User:
#     post = User(username, email, name, is_stuff)
#     await create_posts(session, post)
#     print(f"Created post by {user.user_name} with title: {post.title}")
#     return post


async def create_posts(session: AsyncSession, posts: List[Post]):
    session.add_all(posts)
    await session.commit()
