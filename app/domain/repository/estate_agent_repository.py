import logging

from app.domain.entity.estate_agent import EstateAgent
from app.gateways.databases import gateway_database
from app.gateways.databases.connection import session


def update_agent(agent_id, updated_agent_data):
    agent = get_agent_by_id(agent_id)
    if agent:
        for key, value in updated_agent_data.items():
            setattr(agent, key, value)
        session.merge(agent)
        session.commit()
        return True
    else:
        return False


def get_agent_by_id(agent_id):
    return session.query(EstateAgent).filter_by(id=agent_id).first()


def get_agent_by_name(full_name):
    return session.query(EstateAgent).filter_by(full_name=full_name).first()


def get_all_agent():
    return session.query(EstateAgent).all()


def delete_agent(agent_id):
    agent = session.query(EstateAgent).filter_by(id=agent_id).first()
    if agent:
        agent.active = False
        session.commit()
        return True
    else:
        return False


def create_agent(username, password, full_name, creci):
    agent = EstateAgent(creci, username=username, password=password, full_name=full_name)
    gateway_database.save(agent)
    logging.info("Corretor criado com sucesso no banco de dados")

