from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.models.board import Board
from backend.sqrt_chan.app.repository.base_repo import BaseRepository


class BoardRepository(BaseRepository[Board]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(Board, async_session)
