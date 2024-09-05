from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.company import Company
from schemas.company import CompanySchema

class CompanyService:

    def get_companies(self, db: Session) -> List[Company]:
        query = select(Company)

        return db.scalars(query).all()

    def create_company(self, db: Session, data: CompanySchema) -> Company:
        company = Company(**data.model_dump())

        db.add(company)
        db.commit()
        db.refresh(company)

        return company