from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.sqrt_chan.app.logger import log
import time

from backend.sqrt_chan.controller.board_controller import board
from backend.sqrt_chan.controller.post_controller import reply_post
from backend.sqrt_chan.controller.role_contrellor import role
from backend.sqrt_chan.controller.thread_controller import thread

app = FastAPI(root_path='/api')

@app.middleware('http')
async def log_requests(r: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(r)
    except HTTPException as e:
        log.warning("HTTPException: %s %s - %d %s", r.method, r.url.path, e.status_code, e.detail)
    duration = (time.time() - start_time) * 1000
    log.info(
        '%s %s - status: %d - duration: %.2fms',
        r.method,
        r.url.path,
        response.status_code,
        duration
    )
    return response

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
