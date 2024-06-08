"""add width density to product model int

Revision ID: 9875c218a72f
Revises: d23a2ef85360
Create Date: 2024-06-07 11:08:11.705233

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9875c218a72f"
down_revision: Union[str, None] = "d23a2ef85360"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "density",
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    op.alter_column(
        "products",
        "width",
        existing_type=sa.Integer(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
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
