"""empty message

Revision ID: 833661611a36
Revises: cc980ab598fe
Create Date: 2021-10-18 08:46:49.540912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '833661611a36'
down_revision = 'cc980ab598fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_users_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('repository', sa.String(length=70), nullable=False),
    sa.Column('languages', sa.JSON(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('number_of_repositories', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('github_users_info')
    # ### end Alembic commands ###
