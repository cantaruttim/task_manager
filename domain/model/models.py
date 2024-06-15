from datetime import datetime 

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from .database import Base, engine


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(50))
    status = Column(String(50))
    created_at = Column(String(50), autoincrement=True)

    # task_id = Column(Integer, ForeignKey('enderecos.id', ondelete='CASCADE'))
  

    def create(self, session: Session):
        session.add(self)
        session.commit()
        session.refresh(self)
        return self


    def update(self, session: Session, task_data):
        for key, value in task_data.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)
        return self


    def delete(self, session: Session):
        task_id = self.id
        session.delete(self)
        session.commit()
        return task_id


    def read(self, session: Session, id):
        return session.query(Tasks).filter(Tasks.id == id).first()


    def __repr__(self):
        return f'<Tasks(id={self.id}, title={self.title},  description={self.description}, status={self.status}, created_at ={self.created_at})>'


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
