from fastapi import APIRouter, Depends, Request

from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.schemas.role import Role
from backend.sqrt_chan.app.utils.hash import get_user_ip
from backend.sqrt_chan.app.utils.role import require_moderator
from backend.sqrt_chan.app.utils.session import get_post_service
from backend.sqrt_chan.service.post_service import PostService

reply_post = APIRouter()


@reply_post.post("/{board_slug}/thread/{thread_id}/post", response_model=PostRS)
async def create_new_post(
    r: Request,
    board_slug,
    post_data: PostCS,
    thread_id: int,
    service: PostService = Depends(get_post_service),
):
    ip = get_user_ip(r)
    return await service.create_post(board_slug, thread_id, ip, post_data)


@reply_post.patch("/threads/{thread_id}/{post_id}")
async def update_post_by_id(
    thread_id: int,
    post_id: int,
    post_data: PostUS,
    service: PostService = Depends(get_post_service),
    _: Role = Depends(require_moderator),
):
    return await service.update_post(thread_id, post_id, post_data)
