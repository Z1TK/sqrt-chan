from fastapi import APIRouter, Depends, Request

from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.schemas.post import *
from backend.sqrt_chan.app.utils.hash import get_user_ip
from backend.sqrt_chan.app.utils.session import get_service
from backend.sqrt_chan.service.post_service import PostService

posts = APIRouter(prefix="/posts")


@posts.post("", response_model=PostRS)
async def create_new_post(
    r: Request,
    post_data: PostCS,
    service: PostService = Depends(get_service(PostService, PostRepository)),
):
    ip = get_user_ip(r)
    return await service.create(ip, post_data)


@posts.get("", response_model=list[PostRS])
async def get_all_posts(
    service: PostService = Depends(get_service(PostService, PostRepository))
):
    return await service.get_all_posts()
