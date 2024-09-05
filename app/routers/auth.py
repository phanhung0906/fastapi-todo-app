from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db_context
from services.exception import UnAuthorizedError
from models.user import User
from typing import Annotated
from schemas.user import UserResponseSchema
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db_context)
):
    user = AuthService().authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise UnAuthorizedError()

    return {"access_token": AuthService().create_access_token(user), "token_type": "bearer"}

@router.get("/me/", response_model=UserResponseSchema)
async def read_users_me(
    current_user: Annotated[User, Depends(AuthService().get_current_user)],
):
    return current_user