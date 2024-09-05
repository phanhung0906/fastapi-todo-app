from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class CompanyResponseSchema(BaseModel):
    id: UUID
    name: str
    description: str | None = None
    rating: str | None = None
    mode: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True

class CompanySchema(BaseModel):
    name: str
    description: Optional[str]
    rating: str | None = None
    mode: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Company 1",
                "description": "description Company 1",
                "rating": "1",
                "mode": "1"
            }
        }