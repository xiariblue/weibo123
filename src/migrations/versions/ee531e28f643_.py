"""empty message

Revision ID: ee531e28f643
Revises: 
Create Date: 2019-12-26 21:04:05.242437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee531e28f643'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('city', sa.String(length=16), nullable=True),
    sa.Column('avatar', sa.String(length=128), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_nickname'), 'user', ['nickname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_nickname'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
