
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from upload.app import upload_router

import settings

app = FastAPI()

app.include_router(upload_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS
)

@app.get("/")
async def root():
    return {"message": "Welcome to file server."}


