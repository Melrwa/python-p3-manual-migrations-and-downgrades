"""Renaming students to scholars

Revision ID: b05e1508210c
Revises: 
Create Date: 2024-12-12 07:50:03.303741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b05e1508210c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('students', 'scholars')
    pass


def downgrade():
    op.rename_table('scholars', 'students')

    pass
