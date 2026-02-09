from backend.sqrt_chan.app.repository.board_repo import BoardRepository
from backend.sqrt_chan.app.schemas.board import *


class BoardService:
    def __init__(self, board_repo: BoardRepository):
        self.board_repo = board_repo

    async def all_boards(self) -> list[BoardRS]:
        boards = await self.board_repo.get_all()
        return [BoardRS.model_validate(board).model_dump() for board in boards]

    async def create_board(self, dto: BoardCS) -> BoardRS:
        value = dto.model_dump(exclude_defaults=True)
        res = await self.board_repo.create(**value)
        return BoardRS.model_validate(res).model_dump()
