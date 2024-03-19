from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class House(Base):
    __tablename__ = 'imovel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(500), nullable=False)
    address = Column(String(100), nullable=False)
    number = Column(String(6), nullable=False)
    zip_code = Column(String(9), nullable=False)
    district = Column(String(25), nullable=False)
    city = Column(String(15), nullable=False)
    state = Column(String(15), nullable=False)
    country = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    house_owner_id = Column(Integer, ForeignKey('proprietario.id'), nullable=False)
    estate_agent_id = Column(Integer, ForeignKey('corretor.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default='NOW()')
    active = Column(Boolean, nullable=False)
    photo = Column(String(500), nullable=False)
    views = Column(Integer, nullable=False)

    def __init__(self, description, address, number, zip_code, district, city, state, country, price, status,
                 house_owner_id, created_at, active=True):
        self.description = description
        self.address = address
        self.number = number
        self.zip_code = zip_code
        self.district = district
        self.city = city
        self.state = state
        self.country = country
        self.price = price
        self.status = status
        self.house_owner_id = house_owner_id
        self.created_at = created_at
        self.active = active

    def __str__(self):
        return (f"Referência: {self.id}\nDescrição do imóvel: {self.description}\n"
                f"Localizado no Endereço: {self.address}, {self.number}-{self.zip_code} {self.district} {self.city} {self.state} {self.country}\n"
                f"Valor: R${self.price} | Status: {self.status} | Ativo: {self.active}")
