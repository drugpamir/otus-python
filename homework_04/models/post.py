from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


@dataclass
class PostIn:
    id: int
    userId: int
    title: str
    body: str

    def __init__(self, j: dict):
        self.__dict__.update(j)


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    title = Column(
        String(100),
        nullable=False,
        unique=True,
    )

    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __init__(self, user_id: int, title: str, body: Text):
        self.user_id = user_id
        self.title = title
        self.body = body

    @classmethod
    def from_post_in(cls, post_in: PostIn):
        return cls(
            user_id=post_in.userId,
            title=post_in.title,
            body=post_in.body,
        )

    @classmethod
    def from_json_post_in(cls, j: dict):
        post_in: PostIn = PostIn(j)
        return cls.from_post_in(post_in)

    def __str__(self):
        return f"Post {self.title!r} (id={self.id}, body={self.body!r})"

    def __repr__(self):
        return self.__str__()
