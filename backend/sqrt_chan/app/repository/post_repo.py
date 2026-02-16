from sqlalchemy import and_, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.models.post import Post
from backend.sqrt_chan.app.repository.base_repo import BaseRepository
from backend.sqrt_chan.app.utils.decorators import handler_db_errors


class PostRepository(BaseRepository[Post]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(Post, async_session)

    # @handler_db_errors
    # async def get_all(self, board_slug: str, thread_id: int):
    #     conditions = [
    #         self.model.board_slug == board_slug,
    #         self.model.thread_id == thread_id,
    #         self.model.is_deleted == False,
    #     ]
    #     stmt = select(self.model).where(and_(*conditions))
    #     res = await self.session.execute(stmt)
    #     return res.scalars().all()

    @handler_db_errors
    async def update(self, thread_id: int, post_id, **kwargs):
        condition = [
            self.model.thread_id == thread_id,
            self.model.id == post_id,
        ]
        stmt = (
            update(self.model)
            .where(and_(*condition))
            .values(**kwargs)
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        await self.session.flush()
        return res.scalar_one_or_none()
