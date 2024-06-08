"""add width density to product model

Revision ID: f88348218b1e
Revises: 0537e28c827d
Create Date: 2024-06-07 11:02:02.031739

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f88348218b1e"
down_revision: Union[str, None] = "0537e28c827d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("products", sa.Column("width", sa.String(), nullable=False))
    op.add_column("products", sa.Column("density", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "density")
    op.drop_column("products", "width")
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
