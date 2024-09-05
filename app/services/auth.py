from datetime import timedelta
from typing import Optional
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError
from sqlalchemy import select
from sqlalchemy.orm import Session

from services.utils import get_current_utc_time
from settings import JWT_SECRET, JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from models.user import User
from typing_extensions import Annotated

oa2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")


class AuthService:

    def authenticate_user(self, username: str, password: str, db: Session):
        user = db.scalars(select(User).filter(User.username == username)).first()

        if not user:
            return False
        if not User().verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(self, user: User, expires: Optional[timedelta] = None):
        claims = {
            "username": user.username,
            "email": user.email,
            "id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_admin": user.is_admin,
            "is_active": user.is_active,
        }
        expire = get_current_utc_time() + expires if expires else get_current_utc_time() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        claims.update({"exp": expire})
        return jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM)

    def get_current_user(self, token: str = Depends(oa2_bearer)) -> User:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user = User()
            user.username = payload.get("username")
            user.email = payload.get("email")
            user.id = UUID(payload.get("id"))
            user.first_name = payload.get("first_name")
            user.last_name = payload.get("last_name")
            user.is_admin = payload.get("is_admin")
            user.is_active = payload.get("is_active")

            if user.username is None or user.id is None:
                raise self.token_exception()
            if not user.is_active:
                raise HTTPException(status_code=400, detail="Inactive user")
            return user
        except InvalidTokenError:
            raise self.token_exception()

    # Exceptions
    def token_exception(self):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

