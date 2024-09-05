from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from schemas.company import CompanyResponseSchema

class SearchTaskSchema():
    def __init__(self, name, page, size) -> None:
        self.name = name
        self.page = page
        self.size = size

class TaskResponseSchema(BaseModel):
    id: UUID
    name: str | None = None
    summary: str | None = None
    description: str | None = None
    priority: str | None = None
    user_id: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


class TaskSchema(BaseModel):
    name: str
    summary: str
    description: Optional[str]
    priority: Optional[str]
    user_id: Optional[UUID]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Task 1",
                "summary": "summary Task 1",
                "description": "Description for Task 1",
                "priority": "priority Task 1",
                "user_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }