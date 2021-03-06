"""empty message

Revision ID: d2f921583b68
Revises: 4fc2a587581f
Create Date: 2022-06-02 16:17:38.319333

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2f921583b68'
down_revision = '4fc2a587581f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('title', sa.String(length=200), nullable=False))
    op.add_column('question', sa.Column('content', sa.Text(), nullable=False))
    op.drop_column('question', 'username')
    op.drop_column('question', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('email', mysql.TEXT(), nullable=False))
    op.add_column('question', sa.Column('username', mysql.VARCHAR(length=200), nullable=False))
    op.drop_column('question', 'content')
    op.drop_column('question', 'title')
    # ### end Alembic commands ###
