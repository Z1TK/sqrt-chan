from typing import Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.sqrt_chan.app.database.db import async_session
from backend.sqrt_chan.app.repository.board_repo import BoardRepository
from backend.sqrt_chan.app.repository.post_repo import PostRepository
from backend.sqrt_chan.app.repository.thread_repo import ThreadRepository
from backend.sqrt_chan.service.board_service import BoardService
from backend.sqrt_chan.service.post_service import PostService
from backend.sqrt_chan.service.thread_service import ThreadService


async def get_async_session():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        finally:
            await session.close()


def get_service[R](repo: type[R]) -> Callable[[AsyncSession], R]:
    def _get_service(session: AsyncSession = Depends(get_async_session)) -> R:
        return repo(session)

    return _get_service


def get_post_service(
    post_repo: PostService = Depends(get_service(PostRepository)),
    thread_repo: ThreadRepository = Depends(get_service(ThreadRepository)),
):
    return PostService(post_repo, thread_repo)


def get_thread_service(
    thread_repo: ThreadRepository = Depends(get_service(ThreadRepository)),
    post_repo: PostService = Depends(get_service(PostRepository)),
):
    return ThreadService(thread_repo, post_repo)


def get_board_service(repo: BoardRepository = Depends(get_service(BoardRepository))):
    return BoardService(repo)
