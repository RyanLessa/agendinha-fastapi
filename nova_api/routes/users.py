from fastapi import APIRouter, Depends
from nova_api.controllers import users as users_controller
from nova_api.schemas import CreateUserWithAgendaSchema, UserResponseSchema
from sqlalchemy.orm import Session
from nova_api.settings.database import get_db
from typing import List

router = APIRouter()

@router.post("/create", response_model=UserResponseSchema)
def create_user(user_data: CreateUserWithAgendaSchema, db: Session = Depends(get_db)):
    return users_controller.create_user_with_agenda(db, user_data)


@router.get("/{user_id}", response_model=UserResponseSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return users_controller.get_user_detail(db, user_id)

@router.get("/", response_model=List[UserResponseSchema])
def get_users(db: Session = Depends(get_db)):
    return users_controller.list_users(db)
