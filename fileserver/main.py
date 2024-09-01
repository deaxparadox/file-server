from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



# upload application
from apps.upload.main import upload_router
from apps.download.main import download_router

# setting
from core import settings


# database
from core.database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)





app = FastAPI()

app.include_router(upload_router)
app.include_router(download_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to download file server."}

    