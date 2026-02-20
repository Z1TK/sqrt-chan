from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.post import PostCS
from backend.sqrt_chan.app.schemas.thread import *
from backend.sqrt_chan.app.utils.hash import get_hash_ip


class ThreadService:
    def __init__(self, thread_repo: ThreadRepository, post_repo: PostRepository):
        self.thread_repo = thread_repo
        self.post_repo = post_repo

    async def create_threads(self, board_slug: str, ip: str, dto: ThreadCS):
        value = dto.model_copy(update={'board_slug': board_slug}).model_dump()
        thread = await self.thread_repo.create(**value)
        ip_hash = get_hash_ip(ip, thread.id)
        post = (
            PostCS(content=thread.content, image=thread.image)
            .model_copy(
                update={"is_op": True, "thread_id": thread.id, "ip_hash": ip_hash}
            )
            .model_dump()
        )
        await self.post_repo.create(**post)
        return thread

    async def get_available_threads(self, board_slug: str, limit: int = 20):
        threads = await self.thread_repo.get_all(board_slug, False, limit)
        return [thread for thread in threads]

    async def get_archive_threads(self, board_slug: str, limit: int = 100):
        threads = await self.thread_repo.get_all(board_slug, True, limit)
        return [thread for thread in threads]

    async def get_thread(self, board_slug: str, thread_id: int):
        return await self.thread_repo.get_by_id(board_slug, thread_id)

    async def update_thread(self, board_slug: str, thread_id: int, dto: ThreadUS):
        value = dto.model_dump(exclude_unset=True)
        return await self.thread_repo.update(board_slug, thread_id, **value)

    async def delete_threads(self, board_slug: str, thread_ids: list[int]):
        return await self.thread_repo.remove(board_slug, thread_ids)
