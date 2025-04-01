from datetime import datetime


# Функция для сортировки задач по дате
def sort_tasks_by_datetime(tasks: list):
    return sorted(
        tasks, key=lambda item: datetime.strptime(item["deadline"], "%d-%m-%Y")
    )


# Функция для получения задачи по id
def get_task_by_id(data: list, task_id: int):
    for task in data:
        if task["id"] == task_id:
            return task
