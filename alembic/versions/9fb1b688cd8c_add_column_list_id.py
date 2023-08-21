"""Add column list_id

Revision ID: 9fb1b688cd8c
Revises: a6b6f54f2cff
Create Date: 2023-08-13 14:29:36.484931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fb1b688cd8c'
down_revision = 'a6b6f54f2cff'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.add_column('todos', sa.Column('list_id', sa.Integer(), sa.ForeignKey('todolists.id'), nullable=False))
    op.create_foreign_key(None , 'todos' , 'todolists' , ['list_id'] , ['id'])


def downgrade() -> None:
    op.drop_column('todos', 'list_id')







