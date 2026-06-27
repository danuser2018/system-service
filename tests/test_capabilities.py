import pytest
from fastapi.testclient import TestClient
from src.services.capabilities import CapabilityService, CapabilityList, Capability
from src.controllers.capabilities import CapabilityController
from src.api import create_app

def test_capability_service_defaults():
    # Initial state should be empty
    service = CapabilityService()
    # Reset internal state to ensure clean test
    service._capabilities = []
    
    caps = service.get_capabilities()
    assert len(caps.capabilities) == 0

def test_capability_service_registration():
    service = CapabilityService()
    service._capabilities = []
    
    payload = CapabilityList(capabilities=[
        Capability(id="identity", description="Nova Info"),
        Capability(id="weather", description="Nova Weather")
    ])
    
    success = service.register_capabilities(payload)
    assert success is True
    
    caps = service.get_capabilities()
    assert len(caps.capabilities) == 2
    assert caps.capabilities[0].id == "identity"
    assert caps.capabilities[0].description == "Nova Info"
    assert caps.capabilities[1].id == "weather"
    assert caps.capabilities[1].description == "Nova Weather"

def test_capability_service_replacement():
    service = CapabilityService()
    service._capabilities = []
    
    payload1 = CapabilityList(capabilities=[
        Capability(id="identity", description="Nova Info")
    ])
    service.register_capabilities(payload1)
    
    payload2 = CapabilityList(capabilities=[
        Capability(id="weather", description="Nova Weather")
    ])
    service.register_capabilities(payload2)
    
    caps = service.get_capabilities()
    assert len(caps.capabilities) == 1
    assert caps.capabilities[0].id == "weather"

def test_capability_controller():
    # Controller delegates to service, so we can test with a fresh/mock service if needed or just use default.
    # We will clear service capabilities to ensure isolation.
    service = CapabilityService()
    service._capabilities = []
    controller = CapabilityController(service=service)
    
    assert len(controller.get_capabilities().capabilities) == 0
    
    payload = CapabilityList(capabilities=[
        Capability(id="test", description="desc")
    ])
    res = controller.register_capabilities(payload)
    assert res == {"success": True}
    assert len(controller.get_capabilities().capabilities) == 1

def test_api_capabilities_flow():
    # Clean the service state
    CapabilityService._capabilities = []
    
    app = create_app()
    client = TestClient(app)
    
    # 1. GET initially empty
    response = client.get("/system/capabilities")
    assert response.status_code == 200
    assert response.json() == {"capabilities": []}
    
    # 2. POST register capabilities
    payload = {
        "capabilities": [
            {"id": "identity", "description": "Información sobre Nova"},
            {"id": "weather", "description": "Consultar el tiempo"}
        ]
    }
    response = client.post("/system/capabilities", json=payload)
    assert response.status_code == 200
    assert response.json() == {"success": True}
    
    # 3. GET check capabilities are registered
    response = client.get("/system/capabilities")
    assert response.status_code == 200
    data = response.json()
    assert len(data["capabilities"]) == 2
    assert data["capabilities"][0]["id"] == "identity"
    assert data["capabilities"][0]["description"] == "Información sobre Nova"
    assert data["capabilities"][1]["id"] == "weather"
    assert data["capabilities"][1]["description"] == "Consultar el tiempo"
    
    # 4. POST with invalid payload structure should return 400
    invalid_payload = {
        "caps": [
            {"name": "identity"}
        ]
    }
    response = client.post("/system/capabilities", json=invalid_payload)
    assert response.status_code == 400
    
    # 5. POST with invalid types should return 400
    invalid_payload2 = {
        "capabilities": [
            {"id": 123, "description": "Needs to be string"}
        ]
    }
    response = client.post("/system/capabilities", json=invalid_payload2)
    assert response.status_code == 400
