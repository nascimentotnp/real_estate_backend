from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Payment(Base):
    __tablename__ = "pagamento"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    house_id = Column(Integer, ForeignKey('imovel.id'), nullable=False)
    house_price = Column('valor_propriedade', Float, nullable=False)
    house_sold_price = Column('valor_venda', Float, nullable=False)
    owner_payment = Column('pagamento_proprietario', Float, nullable=False)
    agent_payment = Column('pagamento_agente_corretor', Float, nullable=False)
    broker_payment = Column('pagamento_corretor', Float, nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column('data_criacao', DateTime, nullable=False)
    updated_at = Column('data_alteracao', DateTime, nullable=False, server_default='NOW()')
    active = Column("ativo", Boolean, nullable=False)

    def __init__(self, house_price):
        self.house_price = house_price

