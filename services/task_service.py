from pydantic import parse_obj_as

from domain.dto.dtos import TasksCreateDTO, TasksDTO, TasksUpdateDTO
from domain.model.models import Tasks
from repository.task_repository import ITaskRepository


class ITaskService:

    def create_task(self, task_data: object):
        raise NotImplementedError
    
    def read_task(self, task_id: int):
        raise NotImplementedError
    
    def update_task(self, task_id: int, task_update: object):
        raise NotImplementedError
    
    def delete_user(self, task_id: int):
        raise NotImplementedError
    

class TaskService(ITaskService):


    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository


    def create_task(self, task_data: TasksCreateDTO) -> TasksDTO:
        task = Tasks(**task_data.dict())
        created_task = self.task_repository.create(task)
        return parse_obj_as(TasksDTO, created_task)


    def read_task(self, task_id: int) -> TasksDTO:
        task = self.task_repository.read(task_id)
        if task is None:
            raise Exception("Task não encontrada!")
        return parse_obj_as(TasksDTO, task)
    

    def update_task(self, task_id: int, task_data: TasksUpdateDTO) -> TasksDTO:
        task = self.task_repository.read(task_id)
        if task is None:
            raise Exception("Task não encontrada")
        
        task_data = task_data.dict(exclude_unset=True)
        for key, value in task_data.items():
            setattr(task, key, value)
        updated_task = self.task_repository.update(task, task_data)
        return parse_obj_as(TasksDTO, updated_task)
    

    def delete_task(self, task_id: int) -> int:
        task = self.task_repository.read(task_id)
        if task is None:
            raise Exception('task não encontrada!')
        return self.task_repository.delete(task)
