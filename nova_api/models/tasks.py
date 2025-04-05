import sqlalchemy as sa
from sqlalchemy.orm import relationship

from nova_api.settings.database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    agenda_id = sa.Column(sa.Integer, sa.ForeignKey('agendas.id',
                                                    ondelete='CASCADE'))

    name = sa.Column(sa.String(150))
    detail = sa.Column(sa.String(750), nullable=True)

    agenda = relationship('Agenda', back_populates='tasks')

