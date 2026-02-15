import hashlib

from fastapi import Request

from backend.sqrt_chan.core.config import setting


def get_user_ip(r: Request):
    xff = r.headers.get("X-Forwarded-For")
    if xff:
        return xff.split(",")[0].strip()
    return r.client.host


def get_hash_ip(user_ip: str, thread_id: int):
    data = f"{user_ip}{setting.salt}{thread_id}".encode("utf-8")
    return hashlib.sha256(data).hexdigest()
