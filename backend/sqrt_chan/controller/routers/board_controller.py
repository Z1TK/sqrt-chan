from fastapi import APIRouter, Depends

from backend.sqrt_chan.app.repository.board_repo import BoardRepository
from backend.sqrt_chan.app.schemas.board import *
from backend.sqrt_chan.app.utils.session import get_repository
from backend.sqrt_chan.service.board_service import BoardService

board = APIRouter(prefix="/board")


@board.post("")
async def create_new_board(
    board_data: BoardCS, repo: BoardService = Depends(get_repository(BoardRepository))
):
    return await repo.create_board(board_data)


@board.get("")
async def get_all_boards(repo: BoardService = Depends(get_repository(BoardRepository))):
    return await repo.all_boards()
