from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class PostCS(BaseModel):
    thread_id: int
    content: Annotated[str | None, Field()] = None
    image: Annotated[str | None, Field(max_length=255)] = None
    ip_hash: Annotated[str, Field(max_length=64)]


class PostRS(BaseModel):
    thread_id: int
    number: int
    content: str
    image: str
    ip_hash: str
    is_deleted: bool
    created_at: datetime


class PostUS(BaseModel):
    is_deleted: bool
