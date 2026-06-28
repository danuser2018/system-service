from fastapi import APIRouter
from src.controllers import SystemInfoController
from src.services import SystemInfo

router = APIRouter()
controller = SystemInfoController()

@router.get("/v1/system/info", response_model=SystemInfo)
def get_system_info():
    return controller.get_info()

@router.get("/health")
def get_health():
    return controller.get_health()
