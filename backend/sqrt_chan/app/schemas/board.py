from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from backend.sqrt_chan.app.schemas.thread import ThreadPreview


class BoardCS(BaseModel):
    name: str
    description: str
    is_nsfw: Annotated[bool, Field(default=False)]
    bump_limit: Annotated[int, Field(ge=100, le=500, default=250)]


class BoardRS(BaseModel):
    name: str
    description: str
    is_nsfw: Annotated[bool, Field(default=False)]
    bump_limit: Annotated[int, Field(ge=100, le=500, default=250)]
    threads: list[ThreadPreview]
    created_at: datetime


class BoardUS(BaseModel):
    bump_limit: int | None = None
