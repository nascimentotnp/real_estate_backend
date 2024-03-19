
from sqlalchemy import func

from app.domain.entity.house import House
from app.domain.enum.house_status import HouseStatus
from app.gateways.databases.connection import session


def get_sold_house_price_by_agent(agent_id):

    monthly_sold_price = session.query(func.sum(House.price)).filter(
        House.estate_agent_id == agent_id,
        House.status == HouseStatus.SOLD
    ).scalar()

    return monthly_sold_price
