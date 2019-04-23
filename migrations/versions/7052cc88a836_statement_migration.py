"""statement migration

Revision ID: 7052cc88a836
Revises:
Create Date: 2019-04-22 16:44:30.816121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7052cc88a836'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_statement', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'pitch')
    op.create_foreign_key(None, 'reviews', 'pitches', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.add_column('pitches', sa.Column('pitch', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.drop_column('pitches', 'posted')
    op.drop_column('pitches', 'pitch_statement')
    # ### end Alembic commands ###
