"""update order model add adress info

Revision ID: f41bc5c6be7d
Revises: d15cbafffe60
Create Date: 2024-06-23 19:16:25.608383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f41bc5c6be7d'
down_revision: Union[str, None] = 'd15cbafffe60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('adress', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'adress')
    # ### end Alembic commands ###
