from sqlalchemy import Boolean, Column, String, ForeignKey, Uuid
from sqlalchemy.orm import relationship
from database import Base
from models.base_entity import BaseEntity

from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"])


class User(BaseEntity, Base):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    company_id = Column(Uuid, ForeignKey("company.id"), nullable=True)

    company = relationship('Company', back_populates='users')
    tasks = relationship('Task', back_populates='user')

    def get_password_hash(self, password):
        return bcrypt_context.hash(password)

    def verify_password(self, plain_password, hased_password):
        return bcrypt_context.verify(plain_password, hased_password)
