from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str ='/api/v1'
    DB_URL: str = 'postgresql+asyncpg//alisson:0601@localhost:5432/Health'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
