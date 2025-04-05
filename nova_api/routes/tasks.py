from fastapi import APIRouter, Depends
from nova_api.controllers import tasks as tasks_controller
from nova_api.schemas import CreateTaskSchema, TaskResponseSchema
from sqlalchemy.orm import Session
from nova_api.settings.database import get_db
from typing import List

router = APIRouter()


@router.post("/tasks/", response_model=TaskResponseSchema)
def create_task(task_data: CreateTaskSchema, db: Session = Depends(get_db)):
    return tasks_controller.create_task(db, task_data)


@router.get("/tasks/{task_id}", response_model=TaskResponseSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return tasks_controller.get_task_detail(db, task_id)


@router.get("/tasks/", response_model=List[TaskResponseSchema])
def list_tasks(db: Session = Depends(get_db)):
    return tasks_controller.list_tasks(db)
