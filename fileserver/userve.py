import os
import uvicorn


# fastapi app
from main import app


# SERVER CONFIGURATIONS

RELOAD = False
WORKERS = os.getenv("WORKERS")
if not WORKERS:
    WORKERS = 1
    RELOAD = True
else:
    WORKERS = int(WORKERS)


PORT = os.getenv("PORT")
if not PORT:
    PORT = 8000
else:
    PORT = int(PORT)


# DOCKER CONFIGURATION
DOCKER = os.getenv("DOCKER")
if DOCKER:
    HOST = os.getenv("HOST")

def main():
    if DOCKER:
        uvicorn.run(
            "main:app",
            port=PORT,
            workers=WORKERS,
            host=HOST
        )
    else:    
        uvicorn.run(
            "main:app",
            port=PORT,
            reload=RELOAD,
            workers=WORKERS,
        )
    
if __name__ == "__main__":
    main()