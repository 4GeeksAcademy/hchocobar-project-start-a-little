"""empty message

Revision ID: 1859f704d476
Revises: 8edf91ce430e
Create Date: 2023-08-23 17:24:38.513813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1859f704d476'
down_revision = '8edf91ce430e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
