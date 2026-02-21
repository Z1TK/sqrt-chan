import enum
from pydantic import BaseModel

class Role(str, enum.Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"

class AccessRequest(BaseModel):
    key: str