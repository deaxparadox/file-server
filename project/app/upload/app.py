from typing import Annotated
import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import Response, JSONResponse
from fastapi import status
import aiofiles

import settings

upload_router = APIRouter(
    prefix="/upload",
    tags=['upload']
)

@upload_router.get("/")
async def upload_message():
    return {"message": "upload here, using post method"}

@upload_router.post("/")
async def upload_file(file: UploadFile | None = None):
    
    # If no file uploaded
    if not file:
        return JSONResponse({
            "message": "No file uploaded"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    if file.filename in os.listdir(settings.UPLOAD_DIR):
        
        async with aiofiles.open(os.path.join(settings.UPLOAD_DIR, file.filename), '+ab') as uf:
            await uf.write(await file.read())
    else:
        async with aiofiles.open(os.path.join(settings.UPLOAD_DIR, file.filename), '+ab') as uf:
            await uf.write(await file.read())
        
    return JSONResponse({"filename": file.filename}, status_code=status.HTTP_202_ACCEPTED)