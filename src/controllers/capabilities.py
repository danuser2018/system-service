from src.services import CapabilityService, CapabilityList

class CapabilityController:
    def __init__(self, service: CapabilityService = None):
        self.service = service or CapabilityService()

    def register_capabilities(self, data: CapabilityList) -> dict:
        self.service.register_capabilities(data)
        return {"success": True}

    def get_capabilities(self) -> CapabilityList:
        return self.service.get_capabilities()
