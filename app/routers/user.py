from fastapi import APIRouter, Depends
from database import get_db_context
from sqlalchemy.orm import Session
from schemas.user import UserResponseSchema, UserSchema
from models.user import User
from services.auth import AuthService
from services.user import UserService
from services.exception import AccessDeniedError

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("", response_model=list[UserResponseSchema])
async def get_all_user(db: Session = Depends(get_db_context), user: User = Depends(AuthService().get_current_user)):
    if not user.is_admin:
        raise AccessDeniedError()
    return UserService().get_users(db)


@router.post("", response_model=UserResponseSchema)
async def create_user(
        request: UserSchema,
        db: Session = Depends(get_db_context),
        user: User = Depends(AuthService().get_current_user)
):
    if not user.is_admin:
        raise AccessDeniedError()
    return UserService().create_user(db, request)
