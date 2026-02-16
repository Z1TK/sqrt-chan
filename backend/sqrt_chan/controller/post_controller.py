from fastapi import APIRouter, Depends, Request

from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.utils.hash import get_user_ip
from backend.sqrt_chan.app.utils.session import get_service
from backend.sqrt_chan.service.post_service import PostService

reply_post = APIRouter()


@reply_post.post("/{thread_id}/post", response_model=PostRS)
async def create_new_post(
    r: Request,
    post_data: PostCS,
    thread_id: int,
    service: PostService = Depends(get_service(PostService, PostRepository)),
):
    ip = get_user_ip(r)
    return await service.create(thread_id, ip, post_data)


# @reply_post.get("/{board_slug}/threads/{thread_id}", response_model=list[PostRS])
# async def get_all_posts(
#     board_slug: str,
#     thread_id: int,
#     service: PostService = Depends(get_service(PostService, PostRepository)),
# ):
#     return await service.get_all_posts(board_slug, thread_id)


@reply_post.patch("/threads/{thread_id}/{post_id}", response_model=PostRS)
async def update_post_by_id(
    thread_id: int,
    post_id: int,
    post_data: PostUS,
    service: PostService = Depends(get_service(PostService, PostRepository)),
):
    return await service.update_post(thread_id, post_id, post_data)
