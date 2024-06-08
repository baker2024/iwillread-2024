"""cascade delete itemcard

Revision ID: 39824edfb78e
Revises: cfb565309a12
Create Date: 2024-06-04 23:31:53.312184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39824edfb78e'
down_revision: Union[str, None] = 'cfb565309a12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
