from sqlalchemy import func

from app.domain.entity.house import House
from app.domain.enum.house_status import HouseStatus
from app.gateways.databases.connection import session


def get_value_house_sold(owner_id, start_date=None, end_date=None):
    sold_price = session.query(func.sum(House.price)).filter(
        House.house_owner_id == owner_id,
        House.status == HouseStatus.SOLD,
        House.created_at >= start_date,
        House.created_at <= end_date
    ).scalar()
    return sold_price
