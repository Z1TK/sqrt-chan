import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_user: str
    db_host: str
    db_password: str
    db_port: str
    db_name: str

    salt: str

    model_config = SettingsConfigDict(
        env_file=os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../", ".env")
        ),
        env_ignore_empty=True,
        env_prefix="APP_",
    )

    def get_db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


setting = Settings()
