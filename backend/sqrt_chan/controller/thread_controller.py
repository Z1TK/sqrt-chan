from fastapi import APIRouter, Depends, Request

from backend.sqrt_chan.app.schemas.thread import *
from backend.sqrt_chan.app.utils.depends import get_thread_service
from backend.sqrt_chan.app.utils.hash import get_user_ip
from backend.sqrt_chan.service.thread_service import ThreadService

thread = APIRouter()


@thread.post("/{board_slug}/thread", response_model=ThreadPreview)
async def create_new_thread(
    r: Request,
    board_slug: str,
    thread_data: ThreadCS,
    service: ThreadService = Depends(get_thread_service),
):
    ip = get_user_ip(r)
    return await service.create_threads(board_slug, ip, thread_data)


@thread.get("/{board_slug}/threads", response_model=list[ThreadPreview])
async def get_all_threads(
    board_slug: str,
    service: ThreadService = Depends(get_thread_service),
):
    return await service.get_available_threads(board_slug)


@thread.get("/{board_slug}/archive", response_model=list[ThreadPreview])
async def get_all_threads(
    board_slug: str,
    service: ThreadService = Depends(get_thread_service),
):
    return await service.get_archive_threads(board_slug)


@thread.get("/{board_slug}/threads/{thread_id}", response_model=ThreadRS)
async def get_thread(
    board_slug: str,
    thread_id: int,
    service: ThreadService = Depends(get_thread_service),
):
    return await service.get_thread(board_slug, thread_id)


@thread.patch("/{board_slug}/threads/{thread_id}", response_model=ThreadPreview)
async def update_thread_by_slug(
    board_slug: str,
    thread_id: int,
    thread_data: ThreadUS,
    service: ThreadService = Depends(get_thread_service),
):
    return await service.update_thread(board_slug, thread_id, thread_data)


@thread.delete("/{board_slug}/threads")
async def delete_threads(
    board_slug: str,
    thread_ids: int,
    service: ThreadService = Depends(get_thread_service),
):
    await service.delete_threads(board_slug, thread_ids)
