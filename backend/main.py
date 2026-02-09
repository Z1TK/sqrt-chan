from fastapi import FastAPI

from backend.sqrt_chan.controller.router import router

app = FastAPI()

app.include_router(router)
