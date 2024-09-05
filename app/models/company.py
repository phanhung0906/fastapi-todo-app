from sqlalchemy import Column, String
from database import Base
from models.base_entity import BaseEntity
from sqlalchemy.orm import relationship


class Company(BaseEntity, Base):
    __tablename__ = "company"

    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String)
    mode = Column(String)
    rating = Column(String)

    users = relationship("User", back_populates="company")
