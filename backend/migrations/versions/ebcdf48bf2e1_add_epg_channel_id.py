from alembic import op
import sqlalchemy as sa

revision = "ebcdf48bf2e1"
down_revision = "7e02486d2287"
branch_labels = None
depends_on = None


def upgrade():

    op.add_column(
        "channels",
        sa.Column(
            "epg_channel_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.create_index(
        "ix_channels_epg_channel_id",
        "channels",
        ["epg_channel_id"],
    )


def downgrade():

    op.drop_index(
        "ix_channels_epg_channel_id",
        table_name="channels",
    )

    op.drop_column(
        "channels",
        "epg_channel_id",
    )