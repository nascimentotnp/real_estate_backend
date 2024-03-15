from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    phone = Column('telefone', String, nullable=False)
    full_name = Column('nome_completo', String, nullable=False)

    def __init__(self, username, password, phone, full_name):
        self.username = username
        self.password = password
        self.phone = phone
        self.full_name = full_name
