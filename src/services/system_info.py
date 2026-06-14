from pydantic import BaseModel
from src.config import settings

class SystemInfo(BaseModel):
    name: str
    author: str
    version: str
    description: str

class SystemInfoService:
    def get_system_info(self) -> SystemInfo:
        return SystemInfo(
            name=settings.NOVA_NAME,
            author=settings.NOVA_AUTHOR,
            version=settings.NOVA_VERSION,
            description=settings.NOVA_DESCRIPTION
        )
