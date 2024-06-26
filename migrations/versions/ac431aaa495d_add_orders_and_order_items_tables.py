"""Add orders and order_items tables

Revision ID: ac431aaa495d
Revises: dd4cef4e7674
Create Date: 2024-06-06 10:44:46.095182

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ac431aaa495d"
down_revision: Union[str, None] = "dd4cef4e7674"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("cart_items")
    op.drop_column("order_items", "price")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_items",
        sa.Column(
            "price",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.create_table(
        "cart_items",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("product_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("quantity", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"], ["products.id"], name="cart_items_product_id_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="cart_items_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="cart_items_pkey"),
    )
    # ### end Alembic commands ###
