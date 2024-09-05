from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserSchema

class UserService:

    def get_users(self, db: Session) -> List[User]:
        query = select(User)

        return db.scalars(query).all()

    def create_user(self, db: Session, data: UserSchema) -> User:
        user_data = data.model_dump(exclude={"password"})
        user_data['hashed_password'] = User().get_password_hash(data.password)
        user = User(**user_data)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user