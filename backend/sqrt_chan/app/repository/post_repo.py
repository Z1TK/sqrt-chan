from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.models.post import Post
from backend.sqrt_chan.app.repository.base_repo import BaseRepository

class PostRepository(BaseRepository[Post]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(Post, async_session)
