"""create company table

Revision ID: faf0b5d329ce
Revises: 
Create Date: 2024-08-23 13:49:02.243734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'faf0b5d329ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = op.create_table(
        "company",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("name", sa.String, unique=True, index=True),
        sa.Column("description", sa.String),
        sa.Column("mode", sa.String),
        sa.Column("rating", sa.String),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table("company")
