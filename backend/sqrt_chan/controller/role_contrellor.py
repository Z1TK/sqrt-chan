from fastapi import APIRouter, Body, Response

from backend.sqrt_chan.app.utils.role import set_cookie_role
from backend.sqrt_chan.app.schemas.role import AccessRequest

role = APIRouter()


@role.post("/access")
def get_token(r: Response, body: AccessRequest):
    return set_cookie_role(body.key, r)
