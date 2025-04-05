import sqlalchemy as sa
from sqlalchemy.orm import relationship

from nova_api.settings.database import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    username = sa.Column(sa.String, unique=True)

    agenda = relationship('Agenda', back_populates='user', uselist=False)
