from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Post(Base):
    thread_id: Mapped[int] = mapped_column(ForeignKey("threads.id"))
    number: Mapped[int] = mapped_column(autoincrement=True)
    content: Mapped[str] = mapped_column(Text)
    image: Mapped[str | None] = mapped_column(String(255), nullable=True)
    ip_hash: Mapped[str] = mapped_column(String(64))
    is_deleted: Mapped[bool] = mapped_column(Boolean, server_default="false")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
