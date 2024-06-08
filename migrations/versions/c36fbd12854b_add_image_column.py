"""Add image column

Revision ID: c36fbd12854b
Revises: 16d9f22f3839
Create Date: 2024-06-02 21:55:22.489134

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_storages.integrations.sqlalchemy

from products.models import storage

# revision identifiers, used by Alembic.
revision: str = "c36fbd12854b"
down_revision: Union[str, None] = "16d9f22f3839"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "products",
        sa.Column(
            "image",
            fastapi_storages.integrations.sqlalchemy.FileType(storage=storage),
            nullable=True,
        ),
    )
    op.drop_column("products", "image_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "products",
        sa.Column("image_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_column("products", "image")
    # ### end Alembic commands ###