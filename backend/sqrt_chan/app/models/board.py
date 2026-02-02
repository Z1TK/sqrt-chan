from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, event, Boolean
import slugify
from .base import Base


class Board(Base):
    name: Mapped[str] = mapped_column()
    slug: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(Text)
    is_nsfw: Mapped[bool] = mapped_column(Boolean, server_default='false')

@event.listens_for(Board, 'before_insert')
def generate_slug(mapper, connection, target):
    if target.name:
        target.slug = slugify(target.title)