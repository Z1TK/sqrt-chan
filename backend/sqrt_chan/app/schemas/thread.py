from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from backend.sqrt_chan.app.schemas.post import PostRS


class ThreadCS(BaseModel):
    title: Annotated[str, Field(max_length=255)]
    content: str | None = None
    image: Annotated[str | None, Field(max_length=255)] = None


class ThreadPreview(BaseModel):
    board_slug: str
    id: int
    title: Annotated[str, Field(max_length=255)]
    content: str | None = None
    image: Annotated[str | None, Field(max_length=255)] = None
    is_archived: bool
    bump_count: int
    created_at: datetime


class ThreadRS(ThreadPreview):
    posts: list[PostRS] | None


class ThreadUS(BaseModel):
    title: str | None = None
    content: str | None = None
    image: str | None = None
    is_closed: bool | None = None
    is_archived: bool | None = None
