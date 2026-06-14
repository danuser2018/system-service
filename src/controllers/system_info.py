from src.services import SystemInfoService, SystemInfo

class SystemInfoController:
    def __init__(self, service: SystemInfoService = None):
        self.service = service or SystemInfoService()

    def get_info(self) -> SystemInfo:
        return self.service.get_system_info()

    def get_health(self) -> dict:
        return {"status": "ok"}
