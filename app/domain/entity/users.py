from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = None
    __abstract__ = True

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    phone = Column('telefone', String, nullable=False)
    full_name = Column('nome_completo', String, nullable=False)
    pay = Column('pagamento', String, nullable=False)
    created_at = Column('data_criacao', DateTime, nullable=False)
    updated_at = Column('data_alteracao', DateTime, nullable=False, server_default='NOW()')
    active = Column("ativo", Boolean, nullable=False)

    def __init__(self, username, password, full_name):
        self.username = username
        self.password = password
        self.full_name = full_name
