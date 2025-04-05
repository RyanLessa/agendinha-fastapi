from sqlalchemy.orm import Session
from nova_api.models.user import User
from nova_api.models.agenda import Agenda
from nova_api.schemas import CreateUserWithAgendaSchema


def create_user_with_agenda(db: Session, user_data: CreateUserWithAgendaSchema):
    new_agenda = Agenda(name=user_data.agenda.name)
    new_user = User(username=user_data.username, agenda=new_agenda)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_detail(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("Usuário não encontrado")
    return user

def list_users(db: Session):
    return db.query(User).all()
