from sqlalchemy import select, and_, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.sqrt_chan.app.models.thread import Thread
from backend.sqrt_chan.app.repository.base_repo import BaseRepository
from backend.sqrt_chan.app.utils.decorators import handler_db_errors


class ThreadRepository(BaseRepository[Thread]):
    def __init__(self, async_session):
        super().__init__(Thread, async_session)

    @handler_db_errors
    async def get_all(self, board_slug: str):
        stmt = select(self.model).where(self.model.board_slug == board_slug)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def get_by_id(self, board_slug: str, thread_id: int):
        condition = [self.model.board_slug == board_slug, self.model.id == thread_id]
        stmt = (
            select(self.model)
            .options(selectinload(self.model.posts))
            .where(and_(*condition))
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    @handler_db_errors
    async def update(self, board_slug: str, thread_id: int, **kwargs):
        condition = [self.model.board_slug == board_slug, self.model.id == thread_id]
        stmt = (
            update(self.model)
            .where(and_(*condition))
            .values(**kwargs)
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        await self.session.flush()
        return res.scalar_one_or_none()

    @handler_db_errors
    async def remove(self, board_slug: str, thread_ids: list[int]) -> None:
        condition = [self.model.board_slug == board_slug]
        if len(thread_ids) == 1:
            condition.append(self.model.id == thread_ids[0])
        else:
            condition.append(self.model.id.in_(thread_ids))
        stmt = delete(self.model).where(and_(*condition))
        await self.session.execute(stmt)
        await self.session.flush()
