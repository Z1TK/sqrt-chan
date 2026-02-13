from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.models.thread import Thread
from backend.sqrt_chan.app.repository.base_repo import BaseRepository


class ThreadRepository(BaseRepository[Thread]):
    def __init__(self, async_session):
        super().__init__(Thread, async_session)
