from fastapi import APIRouter, Depends
from database import get_db_context
from sqlalchemy.orm import Session
from services.company import CompanyService
from schemas.company import CompanyResponseSchema, CompanySchema
from models.user import User
from services.auth import AuthService
from services.exception import AccessDeniedError

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("", response_model=list[CompanyResponseSchema])
async def get_all_company(db: Session = Depends(get_db_context)):
    return CompanyService().get_companies(db)


@router.post("", response_model=CompanyResponseSchema)
async def create_company(
        request: CompanySchema,
        db: Session = Depends(get_db_context),
        user: User = Depends(AuthService().get_current_user)
):
    if not user.is_admin:
        raise AccessDeniedError()
    return CompanyService().create_company(db, request)
