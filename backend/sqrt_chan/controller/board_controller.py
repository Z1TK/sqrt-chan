from fastapi import APIRouter, Depends

from backend.sqrt_chan.app.repository.board_repo import BoardRepository
from backend.sqrt_chan.app.schemas.board import *
from backend.sqrt_chan.app.utils.session import get_service
from backend.sqrt_chan.service.board_service import BoardService

board = APIRouter(prefix="/boards")


@board.post("", response_model=BoardPreview)
async def create_new_board(
    board_data: BoardCS,
    service: BoardService = Depends(get_service(BoardService, BoardRepository)),
):
    return await service.create_board(board_data)


@board.get("", response_model=list[BoardPreview])
async def get_all_boards(
    service: BoardService = Depends(get_service(BoardService, BoardRepository))
):
    return await service.all_boards()


@board.get("/{slug}", response_model=BoardRS)
async def get_board_by_slug(
    slug: str,
    service: BoardService = Depends(get_service(BoardService, BoardRepository)),
):
    return await service.get_board(slug)


@board.patch("", response_model=BoardPreview)
async def update_board_by_slug(
    slug: str,
    board_data: BoardUS,
    service: BoardService = Depends(get_service(BoardService, BoardRepository)),
):
    return await service.update_board(slug, board_data)


@board.delete("")
async def delete_board_by_slug(
    slug: str,
    service: BoardService = Depends(get_service(BoardService, BoardRepository)),
):
    await service.delete_board(slug)
