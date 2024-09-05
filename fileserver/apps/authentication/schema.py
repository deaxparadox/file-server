from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRequestSchema(BaseModel):
    username: str
    password: str
    email: EmailStr