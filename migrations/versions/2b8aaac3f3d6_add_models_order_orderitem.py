"""add models order orderitem

Revision ID: 2b8aaac3f3d6
Revises: 9470516460ae
Create Date: 2024-06-06 09:50:20.520869

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2b8aaac3f3d6"
down_revision: Union[str, None] = "9470516460ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
