from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from domain.model.database import get_db
from domain.dto.dtos import TasksDTO, TasksCreateDTO, TasksUpdateDTO
from repository.task_repository import TaskRespository
from services.task_service import TaskService

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_tasks_repo(db: Session = Depends(get_db)) -> TaskRespository:
    return TaskRespository(db)


@task_router.post("/", status_code=201, description="Busca todas as Tarefas", response_model=TasksDTO)
def create(request: TasksCreateDTO, task_repo: TaskRespository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.create_task(request)


@task_router.get("/{task_id}", status_code=200, description="Busca uma tarefa pelo ID", response_model=TasksDTO)
def find_by_id(task_int: int, task_repo: TaskRespository = Depends(get_tasks_repo)):
    user_service = TaskRespository(task_repo)
    return user_service.read_user(task_int)


@task_router.put("/", status_code=200, description="Busca todas as Tarefas", response_model=list[TasksDTO])
def find_all(task_repo: TaskRespository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.find_all()

@task_router.put("/{task_id}", status_code=200, description="Atualiza uma tarefa", response_model=TasksDTO)
def update(task_id: int, request: TasksUpdateDTO, task_repo: TaskRespository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.update_task(task_id, request)

@task_router.delete("/{task_id}", status_code=204, description="Deleta uma tarefa")
def delete(task_id: int, task_repo: TaskRespository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    task_service.delete_task(task_id)
    