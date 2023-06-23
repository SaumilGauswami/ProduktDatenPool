"""first commit

Revision ID: 21814b940bef
Revises: 
Create Date: 2023-06-20 17:13:14.012709

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21814b940bef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Solar',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('manufacturer_no', sa.String(length=255), nullable=True),
    sa.Column('articleNumber', sa.String(length=255), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('breadcrums', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('sitename', sa.String(length=255), nullable=True),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('api_key', sa.String(length=255), nullable=True),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('modified_on', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('Solar')
    # ### end Alembic commands ###
