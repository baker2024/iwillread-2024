"""add models order orderitem

Revision ID: 9470516460ae
Revises: 3edaa0a4b681
Create Date: 2024-06-06 09:31:03.371496

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9470516460ae"
down_revision: Union[str, None] = "3edaa0a4b681"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
