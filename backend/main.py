from fastapi import FastAPI

from backend.sqrt_chan.controller.board_controller import board
from backend.sqrt_chan.controller.post_controller import reply_post
from backend.sqrt_chan.controller.thread_controller import thread

app = FastAPI()

app.include_router(board)
app.include_router(thread)
app.include_router(reply_post)
