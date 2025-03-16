"""Renaming students to scholars

Revision ID: 8b93e5f9ef7f
Revises: 791279dd0760
Create Date: 2025-03-16 10:35:03.957067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b93e5f9ef7f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
