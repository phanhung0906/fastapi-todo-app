"""create user table

Revision ID: 98c78d70bdb4
Revises: faf0b5d329ce
Create Date: 2024-08-23 13:49:07.380812

"""
from typing import Sequence, Union

from alembic import op

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '98c78d70bdb4'
down_revision: Union[str, None] = 'faf0b5d329ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # User Table
    user_table = op.create_table(
        "user",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column('company_id', sa.UUID, nullable=True),
        sa.Column("email", sa.String, unique=True, nullable=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("hashed_password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
        sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    )
    op.create_index("idx_usr_fst_lst_name", "user", ["first_name", "last_name"])


def downgrade() -> None:
    op.drop_table("users")
