"""update product model

Revision ID: 17ee7754008d
Revises: 1a5c645e6433
Create Date: 2024-06-23 16:55:42.282235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17ee7754008d'
down_revision: Union[str, None] = '1a5c645e6433'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'width')
    op.drop_column('products', 'composition')
    op.drop_column('products', 'country')
    op.drop_column('products', 'density')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('density', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('products', sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('products', sa.Column('composition', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('products', sa.Column('width', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
