from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    connection_string: str

settings = Settings()



