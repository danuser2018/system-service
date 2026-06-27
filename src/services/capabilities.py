from pydantic import BaseModel

class Capability(BaseModel):
    id: str
    description: str

class CapabilityList(BaseModel):
    capabilities: list[Capability]

class CapabilityService:
    _capabilities: list[Capability] = []

    def get_capabilities(self) -> CapabilityList:
        return CapabilityList(capabilities=self._capabilities)

    def register_capabilities(self, data: CapabilityList) -> bool:
        self._capabilities = data.capabilities
        return True
