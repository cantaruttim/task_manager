from sqlalchemy.orm import Session

from domain.model.models import Tasks


class ITaskRepository:
    
    def create(self, task: object):
        raise NotImplementedError
    
    def read(self, id: int):
        raise NotImplementedError
    
    def update(self, task: object, task_data: dict):
        raise NotImplementedError
    
    def delete(self, task: object):
        raise NotImplementedError
    


class TaskRespository(ITaskRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(self, task: Tasks) -> Tasks:
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)

    def update(self, task: Tasks, task_data) -> Tasks:

        for key, value in task_data.items():
            setattr(task, key, value)
        self.session.commit()
        self.session.refresh(task)
        return task
    
    def delete(self, task: Tasks) -> int:
        task_id = task.id
        self.session.delete(task)
        self.session.commit()
        return task_id
    
    def read(self, task_id):
        return self.session.query(Tasks).filter(Tasks.id == task_id).first()
        