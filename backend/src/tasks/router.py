from fastapi import APIRouter, HTTPException

from . import service as _service, schemas as _schemas

# Инициализация роутера с тегом и префиксом для группировки endpoint'ов
router = APIRouter(tags=["tasks"], prefix="/tasks")

data = []  # Список для хранения задач в виде словарей
task_id = 1  # Переменная для генерации уникальных идентификаторов


# Маршрут для создания новой задачи
@router.post("/")
def create_task(task: _schemas.Task) -> _schemas.TaskWithID:
    global task_id
    task_dict = task.model_dump()
    task_dict["id"] = task_id
    data.append(task_dict)
    task_id += 1
    return task_dict


# Маршрут для получения всех задач
@router.get("/")
def read_tasks() -> list[_schemas.TaskWithID]:
    return _service.sort_tasks_by_datetime(tasks=data)


# Маршрут для удаления задачи по id
@router.delete("/{task_id}")
def delete_task(task_id: int):
    task = _service.get_task_by_id(data=data, task_id=task_id)
    if task:
        data.remove(task)
        return {"message": f"Task with id {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
