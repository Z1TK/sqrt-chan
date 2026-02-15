from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.utils.hash import get_hash_ip


class PostService:
    def __init__(self, post_repo: PostRepository):
        self.post_repo = post_repo

    async def create(self, user_id: str, dto: PostCS):
        ip_hash = get_hash_ip(user_id, dto.thread_id)
        dto.ip_hash = ip_hash
        value = dto.model_dump()
        return await self.post_repo.create(**value)

    async def get_all_posts(self):
        return await self.post_repo.get_all()
