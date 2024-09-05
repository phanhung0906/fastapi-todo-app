"""create sample data

Revision ID: bd0b6c1e9cfe
Revises: 0000f5a6b0f2
Create Date: 2024-08-23 15:12:31.278020

"""
from typing import Sequence, Union
from models.company import Company

from models.task import Task
from sqlalchemy.orm import Session

from alembic import op

from models.user import User
from settings import ADMIN_DEFAULT_PASSWORD

# revision identifiers, used by Alembic.
revision: str = 'bd0b6c1e9cfe'
down_revision: Union[str, None] = '0000f5a6b0f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    company1 = Company(name="Company A")
    user1 = User(username="user1", first_name="User", last_name="1", email='user1@gmail.com',
                 hashed_password=User().get_password_hash(ADMIN_DEFAULT_PASSWORD),
                 is_admin=True, company=company1)
    user2 = User(username="user2", first_name="User", last_name="2", email='user2@gmail.com',
                 hashed_password=User().get_password_hash(ADMIN_DEFAULT_PASSWORD),
                 company=company1)

    task1 = Task(name="Task 1", description="Description Task 1", user=user1)
    task2 = Task(name="Task 2", description="Description Task 2", user=user1)
    task3 = Task(name="Task 3", description="Description Task 3", user=user1)
    task4 = Task(name="Task 4", description="Description Task 4", user=user2)
    task5 = Task(name="Task 5", description="Description Task 5", user=user2)

    session.add(company1)
    session.add(user1)
    session.add(user2)
    session.add(task1)
    session.add(task2)
    session.add(task3)
    session.add(task4)
    session.add(task5)
    session.commit()


def downgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    session.execute('DELETE FROM task')
    session.execute('DELETE FROM user')
    session.execute('DELETE FROM company')

    session.commit()
