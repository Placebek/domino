import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from core.config_path import BasePath


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=f'{BasePath}/.env', env_file_encoding='utf-8', extra='ignore')

    DB_HOST: str
    DB_PORT: int
    DB_PASS: str
    DB_NAME: str
    DB_USER: str

    TOKEN_SECRET_KEY: str

    def reload_env(self):
        load_dotenv(override=True)

    @property
    def DATABASE_URL_asyncpg(self):
        self.reload_env()
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    TOKEN_ALGORITHM: str = 'HS256'
    TOKEN_EXPIRE_MINUTES: int = 60 * 20  

    DATETIME_FORMAT: str = '%d-%m-%Y %H:%M:%S'


settings = Settings()
