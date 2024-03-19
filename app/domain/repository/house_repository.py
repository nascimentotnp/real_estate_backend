import logging

from app.domain.entity.house import House
from app.domain.enum.house_status import HouseStatus
from app.gateways.databases import gateway_database
from app.gateways.databases.connection import session


def delete_house(house_id):
    house = session.query(House).filter_by(id=house_id).first()
    if house:
        house.active = False
        session.commit()
        return True
    else:
        return False


def get_house_by_id(house_id):
    house = session.query(House).filter_by(id=house_id).first()
    return house


def get_house_by_id_owner(id_owner):
    house = session.query(House).filter_by(house_owner_id=id_owner).first()
    return house


def get_house_by_id_agent(id_agent):
    house = session.query(House).filter_by(estate_agent_id=id_agent).first()
    return house


def get_all_houses():
    return session.query(House).all()


def update_house(house_id, updated_house_data):
    house = get_house_by_id(house_id)
    if house:
        for key, value in updated_house_data.items():
            setattr(house, key, value)
        session.merge(house)
        session.commit()
        return True
    else:
        return False


def create_house(description, address, number, zip_code, district, city, state, country, price, status,
                 house_owner_id, created_at, active=True):
    house = House(description=description, address=address, number=number, zip_code=zip_code, district=district,
                  city=city, state=state, country=country, price=price, status=status, house_owner_id=house_owner_id,
                  created_at=created_at, active=active)
    gateway_database.save(house)
    logging.info("Propriedade criada com sucesso no banco de dados")


def change_house_status(house_id, new_status):
    house = get_house_by_id(house_id)
    if house:
        if isinstance(new_status, HouseStatus):
            house.status = new_status.value
            session.commit()
            return True
        else:
            print("Erro: O novo status fornecido não é válido.")
            return False
    else:
        print("Erro: Não foi possível encontrar a casa para atualizar.")
        return False
