from fastapi import APIRouter, Depends

from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.thread import *
from backend.sqrt_chan.app.utils.session import get_service
from backend.sqrt_chan.service.thread_service import ThreadService

thread = APIRouter(prefix="/api/thread")


@thread.post("", response_model=ThreadPreview)
async def create_new_thread(
    thread_data: ThreadCS,
    service: ThreadService = Depends(get_service(ThreadService, ThreadRepository)),
):
    return await service.create_threads(thread_data)


@thread.get("", response_model=list[ThreadPreview])
async def get_all_threads(
    service: ThreadService = Depends(get_service(ThreadService, ThreadRepository))
):
    return await service.get_threads()
