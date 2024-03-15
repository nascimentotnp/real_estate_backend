from sqlalchemy import Column, String, Integer, ForeignKey

from app.domain.entity.users import User


class EstateAgent(User):
    __tablename__ = 'corretor_imovel'

    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    creci = Column('creci', String, nullable=False, unique=True)
    payment = Column('salario', String, nullable=False)
