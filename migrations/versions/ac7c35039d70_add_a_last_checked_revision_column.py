"""Add a last_checked_revision column

Revision ID: ac7c35039d70
Revises: 90eb9d1f9267
Create Date: 2023-08-16 22:35:25.314490

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ac7c35039d70"
down_revision = "90eb9d1f9267"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "repo", sa.Column("last_checked_revision", sa.String(length=255), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("repo", "last_checked_revision")
    # ### end Alembic commands ###