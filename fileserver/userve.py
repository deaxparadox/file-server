import os
import uvicorn


# fastapi app
from main import app


# CONFIGURATIONS

WORKERS = os.getenv("WORKERS")
if not WORKERS:
    WORKERS = 1
else:
    WORKERS = int(WORKERS)


PORT = os.getenv("PORT")
if not PORT:
    PORT = 8000
else:
    PORT = int(PORT)
    
    
    
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=PORT,
        workers=WORKERS,
    )