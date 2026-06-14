from fastapi import FastAPI
from src.routes import system_info_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Nova System Service",
        description="Servicio de identidad del sistema Nova (Fase 1)",
        version="2.0.0"
    )
    
    # Mount routes
    app.include_router(system_info_router)
    
    return app
