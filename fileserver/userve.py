import uvicorn

from main import app


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=9000,
        workers=5,
        
    )