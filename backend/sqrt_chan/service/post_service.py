from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.utils.hash import get_hash_ip


class PostService:
    def __init__(self, post_repo: PostRepository, thread_repo: ThreadRepository = None):
        self.post_repo = post_repo
        self.thread_repo = thread_repo

    async def create_post(self, board_slug:str, thread_id: int, ip: str, dto: PostCS):
        value = dto.model_dump()
        ip_hash = get_hash_ip(ip, thread_id)
        value["thread_id"] = thread_id
        value["ip_hash"] = ip_hash
        await self.thread_repo.update(board_slug, thread_id, )
        return await self.post_repo.create(**value)

    async def update_post(self, thread_id: int, post_id: int, dto: PostUS):
        value = dto.model_dump(exclude_unset=True)
        return await self.post_repo.update(thread_id, post_id, **value)
