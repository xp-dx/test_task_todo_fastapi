from pydantic import BaseModel, field_validator
from datetime import datetime


# Схема задачи
class Task(BaseModel):
    title: str
    description: str
    deadline: str

    # Валидатор для поля deadline
    @field_validator("deadline")
    @classmethod
    def validate_deadline(cls, value: str) -> str:
        try:
            deadline_date = datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD-MM-YYYY")

        if deadline_date < datetime.now().date():
            raise ValueError("Deadline cannot be in the past")

        return value


# Схема задачи с id
class TaskWithID(Task):
    id: int
