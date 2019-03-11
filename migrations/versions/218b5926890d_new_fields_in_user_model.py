"""new fields in user model

Revision ID: 218b5926890d
Revises: 33b0dd6fd0d9
Create Date: 2019-03-11 16:59:39.863694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218b5926890d'
down_revision = '33b0dd6fd0d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
