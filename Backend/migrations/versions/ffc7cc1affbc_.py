"""empty message

Revision ID: ffc7cc1affbc
Revises: 4bfaf09d12c4
Create Date: 2023-06-04 13:19:46.466827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffc7cc1affbc'
down_revision = '4bfaf09d12c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('Image',
               existing_type=sa.BLOB(),
               type_=sa.String(length=50),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('Image',
               existing_type=sa.String(length=50),
               type_=sa.BLOB(),
               nullable=True)

    # ### end Alembic commands ###
