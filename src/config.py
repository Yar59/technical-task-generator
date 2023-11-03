import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str = 'tt-generator'

    model_config = SettingsConfigDict(
        env_file=os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env'),
        extra='ignore',
    )


settings = Settings()
