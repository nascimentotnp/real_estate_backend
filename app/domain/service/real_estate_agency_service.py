from app.domain.repository.agent_repository import get_sold_house_price_by_agent
from app.domain.repository.house_owner_repository import get_value_house_sold


def calculate_agent_pay(agent_id: int):
    value_house = get_sold_house_price_by_agent(agent_id)
    payment = value_house * 0.1
    return payment


def calculate_house_owner_pay(house_owner_id: int):
    value_house = get_value_house_sold(house_owner_id)
    payment = value_house * 0.85
    return payment


def change_status_to_sold():
    pass


def calculate_depreciation_rate():
    pass


def activate_inactivate():
    pass


def update_photo():
    pass
