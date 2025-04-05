from pydantic import BaseModel, Field
from typing import Optional, List


class AgendaBaseSchema(BaseModel):
    name: str = Field(..., title="Nome da Agenda")


class TaskBaseSchema(BaseModel):
    name: str = Field(..., title="Nome da Tarefa")
    detail: Optional[str] = Field(None, title="Detalhes da Tarefa")


class UserBaseSchema(BaseModel):
    username: str = Field(..., title="Nome de Usuário")


class CreateAgendaSchema(AgendaBaseSchema):
    pass


class CreateTaskSchema(TaskBaseSchema):
    agenda_id: int


class CreateUserSchema(UserBaseSchema):
    pass


class CreateUserWithAgendaSchema(BaseModel):
    username: str = Field(..., title="Nome de Usuário")
    agenda: CreateAgendaSchema


class AgendaResponseSchema(AgendaBaseSchema):
    id: int
    user_id: int
    tasks: List["TaskResponseSchema"] = []

    class Config:
        from_attributes = True


class TaskResponseSchema(TaskBaseSchema):
    id: int
    agenda_id: int

    class Config:
        from_attributes = True


class UserResponseSchema(UserBaseSchema):
    id: int
    agenda: Optional[AgendaResponseSchema] = None

    class Config:
        from_attributes = True


AgendaResponseSchema.update_forward_refs()
