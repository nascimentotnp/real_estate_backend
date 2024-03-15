from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class House(Base):
    __tablename__ = 'imovel'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    address = Column('endereco', String, nullable=False, unique=True)
    number = Column('numero', String, nullable=False)
    zip_code = Column('cep', String, nullable=False)
    price = Column('preco', Float, nullable=False)
    status = Column('cep', String, nullable=False)
    house_owner_id = Column('proprietario_id', ForeignKey('proprietario.id'), primary_key=True)

    def __init__(self, address, number, zip_code):
        self.address = address
        self.password = number
        self.zip_code = zip_code
