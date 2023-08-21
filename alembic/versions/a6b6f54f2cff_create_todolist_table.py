"""create todolist table

Revision ID: a6b6f54f2cff
Revises: 
Create Date: 2023-08-10 14:50:21.209444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6b6f54f2cff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
        'todolists',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )



def downgrade() -> None:
    op.drop_table('todolists')

