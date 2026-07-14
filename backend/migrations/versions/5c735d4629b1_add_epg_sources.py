"""add epg sources

Revision ID: 5c735d4629b1
Revises: ebcdf48bf2e1
Create Date: 2026-07-13

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "5c735d4629b1"
down_revision: Union[str, Sequence[str], None] = "ebcdf48bf2e1"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "epg_sources",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
        ),

        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False,
            unique=True,
        ),

        sa.Column(
            "url",
            sa.String(length=500),
            nullable=False,
        ),

        sa.Column(
            "country",
            sa.String(length=10),
            nullable=True,
        ),

        sa.Column(
            "enabled",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),

        sa.Column(
            "last_download",
            sa.DateTime(),
            nullable=True,
        ),

        sa.Column(
            "last_import",
            sa.DateTime(),
            nullable=True,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
    )

    # SQLite-compatible table rebuild
    with op.batch_alter_table("epg_channels") as batch:

        batch.add_column(
            sa.Column(
                "source_id",
                sa.Integer(),
                nullable=True,
            )
        )


def downgrade() -> None:

    with op.batch_alter_table("epg_channels") as batch:
        batch.drop_column("source_id")

    op.drop_table("epg_sources")