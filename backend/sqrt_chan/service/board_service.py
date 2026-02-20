from backend.sqrt_chan.app.repository.board_repo import BoardRepository
from backend.sqrt_chan.app.schemas.board import *


class BoardService:
    def __init__(self, board_repo: BoardRepository):
        self.board_repo = board_repo

    async def all_boards(self):
        boards = await self.board_repo.get_all()
        return [board for board in boards]

    async def create_board(self, dto: BoardCS):
        value = dto.model_dump()
        return await self.board_repo.create(**value)

    async def update_board(self, board_slug: str, dto: BoardUS):
        value = dto.model_dump(exclude_unset=True)
        return await self.board_repo.update(board_slug, **value)

    async def delete_board(self, board_slug: str):
        return await self.board_repo.remove(model_slug=board_slug)
