from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.routes import system_info_router, capabilities_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Nova System Service",
        description="Servicio de identidad del sistema Nova (Fase 1)",
        version="2.0.0"
    )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse(
            status_code=400,
            content={"detail": exc.errors()}
        )
    
    # Mount routes
    app.include_router(system_info_router)
    app.include_router(capabilities_router)
    
    return app

