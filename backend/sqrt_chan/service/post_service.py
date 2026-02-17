from backend.sqrt_chan.app.repository.board_repo import BoardRepository
from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.utils.hash import get_hash_ip


class PostService:
    def __init__(
        self,
        post_repo: PostRepository,
        thread_repo: ThreadRepository,
        board_repo: BoardRepository,
    ):
        self.post_repo = post_repo
        self.thread_repo = thread_repo
        self.board_repo = board_repo

    async def create_post(self, board_slug: str, thread_id: int, ip: str, dto: PostCS):
        board = await self.board_repo.get_by_slug(board_slug)
        thread = await self.thread_repo.get_by_id(board_slug, thread_id)
        ip_hash = get_hash_ip(ip, thread_id)
        value = dto.model_copy(
            update={"thread_id": thread_id, "ip_hash": ip_hash}
        ).model_dump()
        post = await self.post_repo.create(**value)
        if thread.bump_count <= board.bump_limit:
            await self.thread_repo.bump_update(board_slug, thread_id)
        return post

    async def update_post(self, thread_id: int, post_id: int, dto: PostUS):
        value = dto.model_dump(exclude_unset=True)
        return await self.post_repo.update(thread_id, post_id, **value)
