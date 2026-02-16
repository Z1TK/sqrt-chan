from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.sqrt_chan.app.models.base import Base


class Post(Base):
    thread_id: Mapped[int] = mapped_column(ForeignKey("threads.id"))
    thread: Mapped["Thread"] = relationship("Thread", back_populates="posts")
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    image: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_op: Mapped[bool] = mapped_column(Boolean, server_default="false")
    ip_hash: Mapped[str] = mapped_column(String(64))
    is_deleted: Mapped[bool] = mapped_column(Boolean, server_default="false")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
