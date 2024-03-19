import logging

from app.gateways.databases import gateway_database
from app.gateways.databases.connection import session


def update_entity(entity_class, entity_id, updated_entity_data):
    entity = get_entity_by_id(entity_class, entity_id)
    if entity:
        for key, value in updated_entity_data.items():
            setattr(entity, key, value)
        session.merge(entity)
        session.commit()
        return True
    else:
        return False


def get_entity_by_id(entity_class, entity_id):
    return session.query(entity_class).filter_by(id=entity_id).first()


def get_entity_by_name(entity_class, full_name):
    return session.query(entity_class).filter_by(full_name=full_name).first()


def get_all_entities(entity_class):
    return session.query(entity_class).all()


def delete_entity(entity_class, entity_id):
    entity = session.query(entity_class).filter_by(id=entity_id).first()
    if entity:
        entity.active = False
        session.commit()
        return True
    else:
        return False


def create_entity(entity_class, username, password, full_name, additional_field):
    entity = entity_class(additional_field, username=username, password=password, full_name=full_name)
    gateway_database.save(entity)
    logging.info(f"{entity_class} created successfully in the database")
