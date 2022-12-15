"""in

Revision ID: 3286737e2471
Revises: 3d796fa1bd85
Create Date: 2022-12-14 17:14:29.223121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3286737e2471'
down_revision = '3d796fa1bd85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_stores_id'), 'category_stores', ['id'], unique=False)
    op.drop_constraint('stores_user_id_fkey', 'stores', type_='foreignkey')
    op.drop_constraint('stores_category_id_fkey', 'stores', type_='foreignkey')
    op.drop_column('stores', 'category_id')
    op.drop_column('stores', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stores', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('stores', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('stores_category_id_fkey', 'stores', 'categories', ['category_id'], ['id'])
    op.create_foreign_key('stores_user_id_fkey', 'stores', 'users', ['user_id'], ['id'])
    op.drop_index(op.f('ix_category_stores_id'), table_name='category_stores')
    op.drop_table('category_stores')
    # ### end Alembic commands ###