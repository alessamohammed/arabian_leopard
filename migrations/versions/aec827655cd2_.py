"""empty message

Revision ID: aec827655cd2
Revises: 3527f3f8db7f
Create Date: 2021-11-06 07:38:17.994054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aec827655cd2'
down_revision = '3527f3f8db7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('picture', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('picture', 'name')
    # ### end Alembic commands ###
