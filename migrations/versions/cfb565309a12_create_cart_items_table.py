"""create_cart_items_table

Revision ID: cfb565309a12
Revises: 8f5f1fb39cef
Create Date: 2024-06-03 23:20:57.477161

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cfb565309a12"
down_revision: Union[str, None] = "8f5f1fb39cef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "cart_items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("quantity", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("cart_items")
