from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.sqrt_chan.app.models.base import Base


class Thread(Base):
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))
    title: Mapped[str] = mapped_column(String(255))
    is_closed: Mapped[bool] = mapped_column(Boolean, server_default="false")
    is_archived: Mapped[bool] = mapped_column(Boolean, server_default="false")
    bump_count: Mapped[int] = mapped_column(default=0)
    bump_limit: Mapped[int] = mapped_column(default=100)
    posts: Mapped[list["Post"]] = relationship(
        "Post", back_populates="thread", cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
