from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class PostCS(BaseModel):
    content: Annotated[str | None, Field()] = None
    image: Annotated[str | None, Field(max_length=255)] = None


class PostRS(BaseModel):
    id: int
    thread_id: int
    content: str
    image: str
    ip_hash: str
    is_deleted: bool
    created_at: datetime


class PostUS(BaseModel):
    is_deleted: bool
