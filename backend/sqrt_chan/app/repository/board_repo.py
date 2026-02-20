from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, with_loader_criteria

from backend.sqrt_chan.app.models.board import Board
from backend.sqrt_chan.app.models.thread import Thread
from backend.sqrt_chan.app.repository.base_repo import BaseRepository
from backend.sqrt_chan.app.utils.decorators import handler_db_errors


class BoardRepository(BaseRepository[Board]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(Board, async_session)

    @handler_db_errors
    async def get_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    @handler_db_errors
    async def update(self, board_slug: str, **kwargs):
        stmt = (
            update(self.model)
            .where(self.model.slug == board_slug)
            .values(**kwargs)
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        await self.session.flush()
        return res.scalar_one_or_none()

    @handler_db_errors
    async def remove(self, board_slug) -> None:
        stmt = delete(self.model).where(self.model.slug == board_slug)
        await self.session.execute(stmt)
        await self.session.flush()
