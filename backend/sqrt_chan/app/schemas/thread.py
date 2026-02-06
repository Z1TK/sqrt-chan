from pydantic import BaseModel, Field
from typing import Annotated
from datetime import datetime

from backend.sqrt_chan.app.schemas.post import PostRS

class ThreadCS(BaseModel):
    board_id: int
    title: Annotated[str, Field(max_length=255)]
    content: str | None = None
    image: Annotated[str | None, Field(max_length=255)] = None
    is_closed: bool
    is_achived: bool

class ThreadPreview(BaseModel):
    board_id: int
    title: Annotated[str, Field(max_length=255)]
    content: str | None = None
    image: Annotated[str | None, Field(max_length=255)] = None
    is_closed: bool
    is_achived: bool
    bump_count: int
    created_at: datetime

class ThreadRS(ThreadPreview):
    posts: list[PostRS]

class ThreadUS(BaseModel):
    is_closed: bool| None = None
    is_archived: bool | None = None