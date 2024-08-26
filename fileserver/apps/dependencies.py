from fastapi import Depends, File, UploadFile
from sqlalchemy.orm import Session
from typing import Annotated

from core.database import get_db

class UploadDependency:
    def __init__(self,  db: Annotated[Session, Depends(get_db)], file: Annotated[UploadFile, File(description="Upload a file.")] = None):
        self.file = file
        self.db = db