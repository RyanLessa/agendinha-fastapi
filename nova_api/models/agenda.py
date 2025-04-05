import sqlalchemy as sa
from sqlalchemy.orm import relationship

from nova_api.settings.database import Base


class Agenda(Base):
    __tablename__ = "agendas"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id", ondelete='CASCADE'))

    name = sa.Column(sa.String, unique=True)

    user = relationship('User', back_populates='agenda', uselist=False)
    tasks = relationship('Task', back_populates='agenda')
