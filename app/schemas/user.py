from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from schemas.company import CompanyResponseSchema
from schemas.task import TaskResponseSchema

class UserResponseSchema(BaseModel):
    id: UUID
    username: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool | None = None
    is_admin: bool | None = None
    company_id: UUID | None = None
    company: CompanyResponseSchema | None = None
    tasks: List[TaskResponseSchema] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    is_active: bool
    is_admin: bool
    company_id: UUID | None = None
    password: Optional[str] = None
    hashed_password: Optional[str] = None

    class Config:
        exclude = {"password"}
        json_schema_extra = {
            "example": {
                "email": "email@gmail.com",
                "username": "username",
                "first_name": "first_name",
                "last_name": "last_name",
                "is_active": True,
                "is_admin": True,
                "company_id": "company_id",
                "password": "password",
            }
        }