from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from backend.sqrt_chan.app.schemas.thread import ThreadPreview


class BoardCS(BaseModel):
    name: str
    slug: str
    description: str
    is_nsfw: Annotated[bool, Field(default=False)]
    bump_limit: Annotated[int, Field(ge=100, le=500, default=250)]


class BoardPreview(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    slug: str
    name: str
    description: str
    is_nsfw: Annotated[bool, Field(default=False)]
    bump_limit: Annotated[int, Field(ge=100, le=500, default=250)]
    created_at: datetime


class BoardUS(BaseModel):
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    bump_limit: int | None = None
    is_nsfw: bool | None = None


class BoardRS(BoardPreview):
    model_config = ConfigDict(from_attributes=True)
    threads: list[ThreadPreview] | None
