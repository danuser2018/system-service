from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NOVA_NAME: str = "Nova"
    NOVA_AUTHOR: str = "Xeretre studios"
    NOVA_VERSION: str = "2.0.0"
    NOVA_DESCRIPTION: str = "Asistente personal de voz y automatización"
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
