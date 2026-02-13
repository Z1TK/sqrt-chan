from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.thread import *


class ThreadService:
    def __init__(self, thread_repo: ThreadRepository):
        self.thread_repo = thread_repo

    async def create_threads(self, dto: ThreadCS):
        value = dto.model_dump()
        return await self.thread_repo.create(**value)

    async def get_threads(self):
        threads = await self.thread_repo.get_all()
        return [thread for thread in threads]
