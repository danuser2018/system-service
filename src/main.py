import uvicorn
from src.config import settings
from src.api import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=False  # Disabled reload in production/docker to prevent resource wastage
    )
