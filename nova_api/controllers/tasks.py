from sqlalchemy.orm import Session
from nova_api.models.tasks import Task
from nova_api.schemas import CreateTaskSchema


def create_task(db: Session, task_data: CreateTaskSchema):
    new_task = Task(
        name=task_data.name,
        detail=task_data.detail,
        agenda_id=task_data.agenda_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_task_detail(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise ValueError("Task não encontrada")
    return task


def list_tasks(db: Session):
    return db.query(Task).all()
