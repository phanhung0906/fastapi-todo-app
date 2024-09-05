from sqlalchemy import Column, String, ForeignKey, Uuid
from database import Base
from models.base_entity import BaseEntity
from sqlalchemy.orm import relationship


class Task(BaseEntity, Base):
    __tablename__ = "task"

    name = Column(String, unique=True, index=True)
    summary = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    user_id = Column(Uuid, ForeignKey("user.id"), nullable=True)

    user = relationship('User', back_populates='tasks')