from fastapi import APIRouter, Depends, Request

from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.utils.depends import get_post_service
from backend.sqrt_chan.app.utils.hash import get_user_ip
from backend.sqrt_chan.service.post_service import PostService
from backend.sqrt_chan.service.thread_service import ThreadService

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


# @reply_post.get("/{board_slug}/threads/{thread_id}", response_model=list[PostRS])
# async def get_all_posts(
#     board_slug: str,
#     thread_id: int,
#     service: PostService = Depends(get_service(PostService, PostRepository)),
# ):
#     return await service.get_all_posts(board_slug, thread_id)


@reply_post.patch("/threads/{thread_id}/{post_id}")
async def update_post_by_id(
    thread_id: int,
    post_id: int,
    post_data: PostUS,
    service: PostService = Depends(get_post_service),
):
    return await service.update_post(thread_id, post_id, post_data)
