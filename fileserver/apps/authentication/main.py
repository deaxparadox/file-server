from fastapi import APIRouter, Response, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from apps.upload.helpers import generate_id
from apps.authentication import cruds, schema
from core.database import get_db


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth", "authentication"],
    
)


@auth_router.get("/")
async def authentication_root(db: Session =  Depends(get_db)):
    users = await cruds.get_all_user(db)
    
    
    if isinstance(users, dict):
        return JSONResponse({}, status_code=status.HTTP_200_OK)

    if isinstance(users, list):
        return Response(
            {"users", users},
            status_code=status.HTTP_200_OK
        )
        
@auth_router.post("/create_user/")
async def create_user(user_schema: schema.UserRequestSchema):
    print(user_schema.model_dump())
    
    # password = generate_id(40)
    # user_schema = schema.UserRequestSchema(username=username, password=password, email=email)
    # new_user = await cruds.create_user(user_schema, session)
    # return Response({"user": new_user}, status_code=status.HTTP_201_CREATED)
    return {}