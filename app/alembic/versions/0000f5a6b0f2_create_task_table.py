"""create task table

Revision ID: 0000f5a6b0f2
Revises: 98c78d70bdb4
Create Date: 2024-08-23 13:49:11.786366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0000f5a6b0f2'
down_revision: Union[str, None] = '98c78d70bdb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = op.create_table(
        "task",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column('user_id', sa.UUID, nullable=True),
        sa.Column("name", sa.String, unique=True, index=True),
        sa.Column("summary", sa.String),
        sa.Column("description", sa.String),
        sa.Column("priority", sa.String),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    )


def downgrade() -> None:
    op.drop_table("task")
