from fastapi import APIRouter

from backend.sqrt_chan.controller.routers.board_controller import board

router = APIRouter(prefix="/api")
router.include_router(board)
