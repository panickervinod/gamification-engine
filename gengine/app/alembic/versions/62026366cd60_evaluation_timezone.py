"""evaluation_timezone

Revision ID: 62026366cd60
Revises: 87dfedb58883
Create Date: 2017-02-17 13:54:40.545893

"""

# revision identifiers, used by Alembic.
revision = '62026366cd60'
down_revision = '87dfedb58883'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('achievements', sa.Column('evaluation_timezone', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('achievements', 'evaluation_timezone')
    ### end Alembic commands ###
