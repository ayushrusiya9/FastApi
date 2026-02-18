# write all code OF THIS FILE NEED FOR SETTINGS 
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class Settings(BaseSettings):
    # app
    APP_NAME:str = "FastAPI"

    # database 
    DATABASE_URL:PostgresDsn

    # security 
    SECRET_KEY:str
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30

    class Config:
        env_file = ".env"

# singleston instance 
settings = Settings()
