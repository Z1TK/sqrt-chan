from fastapi import FastAPI

from backend.sqrt_chan.controller.board_controller import board

app = FastAPI()

app.include_router(board)
