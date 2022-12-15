"""in

Revision ID: 6a41e835476c
Revises: 3286737e2471
Create Date: 2022-12-14 17:18:05.665831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a41e835476c'
down_revision = '3286737e2471'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stores', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stores', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stores', type_='foreignkey')
    op.drop_column('stores', 'user_id')
    # ### end Alembic commands ###