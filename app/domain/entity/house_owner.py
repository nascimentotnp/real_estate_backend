from sqlalchemy import Column, ForeignKey, Integer

from app.domain.entity.users import User


class HouseOwner(User):
    __tablename__ = 'proprietario'

    id = Column('cpf', Integer, primary_key=True, nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)



