"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

__all__ = (
    "engine",
    "Session",
    "Base",
    "User",
    "Post",
)

from .db import Base, engine, Session
from .user import User
from .post import Post
