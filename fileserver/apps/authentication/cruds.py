from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List


from apps.authentication.schema import UserRequestSchema
from apps.authentication.models import UserModel

async def get_all_user(db: Session) -> List[UserModel] | dict:
    users = db.query(UserModel).all()
    if len(users) == 0:
        return {}
    return users

async def create_user(user_schema: UserRequestSchema, session: Session):
    user = UserModel(user_schema.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
