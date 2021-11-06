"""empty message

Revision ID: ad10511474be
Revises: 72e106c4a528
Create Date: 2021-11-06 07:58:40.834509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad10511474be'
down_revision = '72e106c4a528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('picture', sa.Column('Image', sa.Text(), nullable=False))
    op.drop_column('picture', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('picture', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('picture', 'Image')
    # ### end Alembic commands ###