from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.thread import *


class ThreadService:
    def __init__(self, thread_repo: ThreadRepository):
        self.thread_repo = thread_repo

    async def create_threads(self, board_slug: str, dto: ThreadCS):
        value = dto.model_dump()
        value["board_slug"] = board_slug
        return await self.thread_repo.create(**value)

    async def get_threads(self, board_slug: str):
        threads = await self.thread_repo.get_all(board_slug)
        return [thread for thread in threads]

    async def get_thread(self, board_slug: str, thread_id: int):
        return await self.thread_repo.get_by_id(board_slug, thread_id)

    async def update_thread(self, board_slug: str, thread_id: int, dto: ThreadUS):
        value = dto.model_dump(exclude_unset=True)
        return await self.thread_repo.update(board_slug, thread_id, **value)

    async def delete_threads(self, board_slug: str, thread_ids: list[int]):
        return await self.thread_repo.remove(board_slug, thread_ids)
