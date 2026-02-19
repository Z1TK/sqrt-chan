import enum


class Role(str, enum.Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
