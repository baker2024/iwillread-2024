""add models order orderitem

Revision ID: 3edaa0a4b681
Revises: 39824edfb78e
Create Date: 2024-06-06 09:28:39.770023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3edaa0a4b681'
down_revision: Union[str, None] = '39824edfb78e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
