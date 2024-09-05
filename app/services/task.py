from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import SearchTaskSchema, TaskSchema
from uuid import UUID
from services.exception import ResourceNotFoundError


class TaskService:

    def get_tasks(self, db: Session, conds: SearchTaskSchema) -> List[Task]:
        query = select(Task)

        if conds.name is not None:
            query = query.filter(Task.name.like(f"{conds.name}%"))

        query = query.offset((conds.page - 1) * conds.size).limit(conds.size)

        return db.scalars(query).all()

    def get_task_by_id(self, db: Session, id: UUID) -> Task:
        query = select(Task).filter(Task.id == id)

        return db.scalars(query).first()

    def create_task(self, db: Session, data: TaskSchema) -> Task:
        task = Task(**data.model_dump())

        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    def update_task(self, db: Session, id: UUID, data: TaskSchema) -> Task:
        task = self.get_task_by_id(db, id)

        if task is None:
            raise ResourceNotFoundError()

        for field, value in data.dict().items():
            if hasattr(task, field) and getattr(task, field) != value:
                setattr(task, field, value)

        db.commit()
        db.refresh(task)

        return task

    def delete_task(self, db: Session, id: UUID) -> None:
        task = self.get_task_by_id(db, id)

        if task is None:
            raise ResourceNotFoundError()

        db.delete(task)
        db.commit()
