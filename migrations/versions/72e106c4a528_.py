"""empty message

Revision ID: 72e106c4a528
Revises: aec827655cd2
Create Date: 2021-11-06 07:57:38.488762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72e106c4a528'
down_revision = 'aec827655cd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('picture', 'image',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('picture', 'image',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
