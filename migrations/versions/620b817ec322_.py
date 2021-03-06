"""empty message

Revision ID: 620b817ec322
Revises: 
Create Date: 2021-10-18 22:05:48.626981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '620b817ec322'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=70), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.add_column('pelicula', sa.Column('genero_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pelicula', 'genero', ['genero_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pelicula', type_='foreignkey')
    op.drop_column('pelicula', 'genero_id')
    op.drop_table('genero')
    # ### end Alembic commands ###
