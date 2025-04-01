from fastapi import FastAPI
from .tasks import router as _tasks_router

# Инициализация FastAPI приложения с метаданными
app = FastAPI(title="ToDo", description="Test task", version="0.0.1")

# Подключение роутера задач к основному приложению
app.include_router(_tasks_router.router)
