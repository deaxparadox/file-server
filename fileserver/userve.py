import os
import uvicorn


# fastapi app
from main import app


# CONFIGURATIONS

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

def main():
    uvicorn.run(
        "main:app",
        port=PORT,
        reload=RELOAD,
        workers=WORKERS,
    )
    
if __name__ == "__main__":
    main()