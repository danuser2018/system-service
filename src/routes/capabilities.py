from fastapi import APIRouter
from src.controllers import CapabilityController
from src.services import CapabilityList

router = APIRouter()
controller = CapabilityController()

@router.post("/system/capabilities")
def register_capabilities(data: CapabilityList):
    return controller.register_capabilities(data)

@router.get("/system/capabilities", response_model=CapabilityList)
def get_capabilities():
    return controller.get_capabilities()
