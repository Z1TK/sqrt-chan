from fastapi import FastAPI

from backend.sqrt_chan.controller.board_controller import board
from backend.sqrt_chan.controller.thread_controller import thread
from backend.sqrt_chan.controller.post_controller import posts

app = FastAPI()

app.include_router(board)
app.include_router(thread)
# app.include_router(posts)
