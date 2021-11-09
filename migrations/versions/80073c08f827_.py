"""empty message

Revision ID: 80073c08f827
Revises: 
Create Date: 2021-11-09 17:52:42.971947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80073c08f827'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('picture_path', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('date_pitched', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('downvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitc_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitc_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('upvote')
    op.drop_table('downvote')
    op.drop_table('comment')
    op.drop_table('pitch')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###