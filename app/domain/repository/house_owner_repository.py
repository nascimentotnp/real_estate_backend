import logging

from app.domain.entity.house_owner import HouseOwner
from app.gateways.databases import gateway_database
from app.gateways.databases.connection import session


def update_owner_house(owner_house, updated_owner_house_data):
    owner_house = get_owner_house_by_id(owner_house)
    if owner_house:
        for key, value in updated_owner_house_data.items():
            setattr(owner_house, key, value)
        session.merge(owner_house)
        session.commit()
        return True
    else:
        return False


def get_owner_house_by_id(owner_house_id):
    return session.query(HouseOwner).filter_by(id=owner_house_id).first()


def get_owner_house_by_name(full_name):
    return session.query(HouseOwner).filter_by(full_name=full_name).first()


def get_all_owner_house():
    return session.query(HouseOwner).all()


def delete_owner_house(owner_house_id):
    owner_house = session.query(HouseOwner).filter_by(id=owner_house_id).first()
    if owner_house:
        owner_house.active = False
        session.commit()
        return True
    else:
        return False


def create_owner_house(username, password, full_name, cpf):
    owner_house = HouseOwner(cpf, username=username, password=password, full_name=full_name)
    gateway_database.save(owner_house)
    logging.info("Corretor criado com sucesso no banco de dados")