from fastapi import APIRouter, Depends, Response

from backend.sqrt_chan.app.utils.role import set_cookie_role

role = APIRouter()


@role.post("/access")
def get_token(r: Response, key: str):
    return set_cookie_role(key, r)
