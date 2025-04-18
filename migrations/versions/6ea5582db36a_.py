"""empty message

Revision ID: 6ea5582db36a
Revises: ec6ac18df512
Create Date: 2025-04-10 02:21:41.972719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ea5582db36a'
down_revision = 'ec6ac18df512'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company', sa.String(length=32), nullable=True))

    with op.batch_alter_table('my_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('summary', sa.Text(length=1024), nullable=True))

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('github_url', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('github_url')

    with op.batch_alter_table('my_info', schema=None) as batch_op:
        batch_op.drop_column('summary')
        batch_op.drop_column('location')

    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.drop_column('company')

    # ### end Alembic commands ###
