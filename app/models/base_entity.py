from sqlalchemy import Column, Uuid, Time
import enum
import uuid
from services.utils import get_current_utc_time

class Gender(enum.Enum):
    NONE = 'N'
    FEMALE = 'F'
    MALE = 'M'


class BaseEntity:
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at = Column(Time, nullable=False, default=get_current_utc_time)
    updated_at = Column(Time, nullable=False, default=get_current_utc_time)
