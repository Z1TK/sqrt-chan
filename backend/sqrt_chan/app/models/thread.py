from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, func, ForeignKey
from datetime import datetime

class Thread(Base):
    board_id: Mapped[int] = mapped_column(ForeignKey('boards.id'))
    title: Mapped[str] = mapped_column(String(255))
    is_closed: Mapped[bool] = mapped_column(Boolean, server_default='false')
    is_archived: Mapped[bool] = mapped_column(Boolean, server_default='false')
    bump_count = Mapped[int] = mapped_column(default=0)
    bump_limit = Mapped[int] = mapped_column(default=100)
    created_at = mapped_column[datetime] = mapped_column(server_default=func.now())
