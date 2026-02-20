from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.sqrt_chan.controller.board_controller import board
from backend.sqrt_chan.controller.post_controller import reply_post
from backend.sqrt_chan.controller.role_contrellor import role
from backend.sqrt_chan.controller.thread_controller import thread

app = FastAPI(openapi_prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(board)
app.include_router(thread)
app.include_router(reply_post)
app.include_router(role)
