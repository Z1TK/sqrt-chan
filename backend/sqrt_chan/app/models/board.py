from datetime import datetime

from slugify import slugify
from sqlalchemy import Boolean, Integer, Text, event, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.sqrt_chan.app.models.base import Base
from backend.sqrt_chan.app.models.thread import Thread


class Board(Base):
    name: Mapped[str] = mapped_column()
    slug: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(Text)
    is_nsfw: Mapped[bool] = mapped_column(Boolean, server_default="false")
    bump_limit: Mapped[int] = mapped_column(Integer)
    threads: Mapped["Thread"] = relationship(
        "Thread", back_populates="board", cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


@event.listens_for(Board, "before_insert")
def generate_slug(mapper, connection, target):
    if target.name:
        target.slug = slugify(target.name)
