from sqlalchemy import Column, String, Integer, ForeignKey

from app.domain.entity.users import User


class EstateAgent(User):
    __tablename__ = 'corretor'

    id = Column('creci', Integer, primary_key=True, nullable=False, unique=True)
    agent_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)

    def __init__(self, id, username, password, full_name):
        super().__init__(username, password, full_name)
        self.id = id
