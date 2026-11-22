from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

CORE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    RMQ_HOST: str
    RMQ_PORT: int
    RMQ_USER: str
    RMQ_PASS: str

    @property
    def RMQ_URL(self):
        return (
            f"amqp://{self.RMQ_USER}:{self.RMQ_PASS}@{self.RMQ_HOST}:{self.RMQ_PORT}//"
        )

    model_config = SettingsConfigDict(env_file=CORE_DIR / ".env")


settings = Settings()  # type: ignore
