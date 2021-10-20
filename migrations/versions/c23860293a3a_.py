"""empty message

Revision ID: c23860293a3a
Revises: 09703a7824e4
Create Date: 2021-10-19 18:12:23.591858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c23860293a3a'
down_revision = '09703a7824e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('horario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('horaInicio', sa.Time(), nullable=True),
    sa.Column('horaFin', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sala',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidadSillas', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calificacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comentario', sa.String(length=70), nullable=True),
    sa.Column('valor', sa.Integer(), nullable=True),
    sa.Column('id_pelicula', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_pelicula'], ['pelicula.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('comentario')
    )
    op.create_table('cartelera',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('FechaInicio', sa.String(length=70), nullable=True),
    sa.Column('FechaFin', sa.Integer(), nullable=True),
    sa.Column('id_pelicula', sa.Integer(), nullable=True),
    sa.Column('id_horario', sa.Integer(), nullable=True),
    sa.Column('id_sala', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_horario'], ['horario.id'], ),
    sa.ForeignKeyConstraint(['id_pelicula'], ['pelicula.id'], ),
    sa.ForeignKeyConstraint(['id_sala'], ['sala.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('FechaInicio')
    )
    op.create_table('compras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Sillas', sa.String(length=70), nullable=True),
    sa.Column('valor', sa.Integer(), nullable=True),
    sa.Column('id_pelicula', sa.Integer(), nullable=True),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_pelicula'], ['pelicula.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Sillas')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('compras')
    op.drop_table('cartelera')
    op.drop_table('calificacion')
    op.drop_table('sala')
    op.drop_table('horario')
    # ### end Alembic commands ###