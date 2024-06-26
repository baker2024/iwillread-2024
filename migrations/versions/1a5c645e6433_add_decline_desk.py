"""add decline desk

Revision ID: 1a5c645e6433
Revises: 092b888e3126
Create Date: 2024-06-19 23:03:33.756678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a5c645e6433'
down_revision: Union[str, None] = '092b888e3126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('decline_desc', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'decline_desc')
    # ### end Alembic commands ###
