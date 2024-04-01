from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, false, func
from sqlalchemy.orm import relationship

from .db import Base


@dataclass
class UserIn:
    id: int
    name: str
    username: str
    email: str

    def __init__(self, j: dict):
        self.__dict__.update(j)


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(100),
        nullable=True,
    )

    username = Column(
        String(32),
        nullable=False,
        unique=True,
    )

    email = Column(
        String(100),
        nullable=True,
        unique=True,
    )

    is_stuff = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default=false(),
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __init__(self, username: str, email: str, name: str = None, is_stuff: bool = False):
        self.username = username
        self.email = email
        self.name = name
        self.is_stuff = is_stuff

    @classmethod
    def from_user_in(cls, user_in: UserIn):
        return cls(
            username=user_in.username,
            email=user_in.email,
            name=user_in.name,
        )

    @classmethod
    def from_json_user_in(cls, j: dict):
        user_in: UserIn = UserIn(j)
        return cls.from_user_in(user_in)

    def __str__(self):
        return f"User {self.username!r} (id={self.id}, name={self.name})"

    def __repr__(self):
        return self.__str__()
