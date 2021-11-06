"""empty message

Revision ID: 3527f3f8db7f
Revises: 039ed7169687
Create Date: 2021-11-06 06:24:44.071644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3527f3f8db7f'
down_revision = '039ed7169687'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('picture', sa.Column('mimetype', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('picture', 'mimetype')
    # ### end Alembic commands ###
