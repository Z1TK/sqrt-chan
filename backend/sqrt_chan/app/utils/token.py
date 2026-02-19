from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Request

from backend.sqrt_chan.core.config import setting


def create_token(role: str, expire_delta: timedelta = timedelta(hours=2)):
    expire = datetime.now(timezone.utc) + expire_delta
    payload = {"role": role, "exp": expire}
    return jwt.encode(payload, setting.key, algorithm=setting.algorithm)
