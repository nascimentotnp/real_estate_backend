from sqlalchemy import Column, ForeignKey, Integer, String

from app.domain.entity.users import User


class HouseOwner(User):
    __tablename__ = 'proprietario'

    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    cpf = Column('cpf', String, nullable=False, unique=True)


