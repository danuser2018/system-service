import pytest
from fastapi.testclient import TestClient

from src.config.config import Settings
from src.services import SystemInfoService
from src.controllers import SystemInfoController
from src.api import create_app

def test_config_defaults():
    # Test that settings can be instantiated with default values
    settings = Settings()
    assert settings.NOVA_NAME == "Nova"
    assert settings.NOVA_AUTHOR == "David"
    assert settings.NOVA_VERSION == "2.0.0"
    assert settings.NOVA_DESCRIPTION == "Asistente personal de voz y automatización"

def test_system_info_service():
    service = SystemInfoService()
    info = service.get_system_info()
    assert info.name == "Nova"
    assert info.author == "David"
    assert info.version == "2.0.0"
    assert info.description == "Asistente personal de voz y automatización"

def test_system_info_controller():
    controller = SystemInfoController()
    info = controller.get_info()
    assert info.name == "Nova"
    health = controller.get_health()
    assert health == {"status": "ok"}

def test_api_endpoints():
    app = create_app()
    client = TestClient(app)
    
    # Test GET /health
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
    # Test GET /system/info
    response = client.get("/system/info")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Nova"
    assert data["author"] == "David"
    assert data["version"] == "2.0.0"
    assert data["description"] == "Asistente personal de voz y automatización"
