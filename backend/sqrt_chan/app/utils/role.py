import jwt
from fastapi import Cookie, Depends, HTTPException, Response

from backend.sqrt_chan.app.schemas.role import Role
from backend.sqrt_chan.app.utils.token import create_token
from backend.sqrt_chan.core.config import setting


def get_role(key: str):
    if key == setting.admin_key:
        return Role.ADMIN
    elif key == setting.moder_key:
        return Role.MODERATOR
    raise HTTPException(403, "Bad Key")


def set_cookie_role(key: str, r: Response):
    role = get_role(key)
    access_token = create_token(role)

    r.set_cookie(
        "access_token", access_token, httponly=True, secure=True, samesite="strict"
    )
    return {"role": role}


def get_role_from_cookie(access_token: str | None = Cookie(None)):
    try:
        payload = jwt.decode(
            access_token, setting.key, setting.algorithm, options={"verify_exp": True}
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Bad token")
    return Role(payload["role"])


def require_admin(role: Role = Depends(get_role_from_cookie)):
    if role != Role.ADMIN:
        raise HTTPException(403, "Admin only")
    return


def require_moderator(role: Role = Depends(get_role_from_cookie)):
    if role not in (Role.ADMIN, Role.MODERATOR):
        raise HTTPException(403, "Moderator only")
    return
