from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.sqrt_chan.app.models.board import Board
from backend.sqrt_chan.app.repository.base_repo import BaseRepository
from backend.sqrt_chan.app.utils.decorators import handler_db_errors


class BoardRepository(BaseRepository[Board]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(Board, async_session)

    @handler_db_errors
    async def get_by_id(self, model_id: int):
        stmt = select(self.model).filter_by(id=model_id)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()
