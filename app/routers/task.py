from fastapi import APIRouter, Depends, Query
from database import get_db_context
from sqlalchemy.orm import Session
from schemas.task import TaskResponseSchema, SearchTaskSchema, TaskSchema
from services.task import TaskService
from uuid import UUID
from services.exception import ResourceNotFoundError
from models import User
from services.auth import AuthService

router = APIRouter(prefix="/task", tags=["Task"])


@router.get("", response_model=list[TaskResponseSchema])
async def get_all_task(name: str = Query(default=None),
                       page: int = Query(ge=1, default=1),
                       size: int = Query(ge=1, le=50, default=10),
                       db: Session = Depends(get_db_context)):
    conds = SearchTaskSchema(name, page, size)
    return TaskService().get_tasks(db, conds)


@router.get("/{task_id}", response_model=TaskResponseSchema)
async def get_task_detail(task_id: UUID, db: Session = Depends(get_db_context),
                          user: User = Depends(AuthService().get_current_user)):
    task = TaskService().get_task_by_id(db, task_id)

    if task is None:
        raise ResourceNotFoundError()

    return task


@router.post("", response_model=TaskResponseSchema)
async def create_task(
        request: TaskSchema,
        db: Session = Depends(get_db_context),
        user: User = Depends(AuthService().get_current_user)
):
    return TaskService().create_task(db, request)


@router.put("/{task_id}", response_model=TaskResponseSchema)
async def update_task(
        task_id: UUID,
        request: TaskSchema,
        db: Session = Depends(get_db_context),
        user: User = Depends(AuthService().get_current_user)
):
    return TaskService().update_task(db, task_id, request)


@router.delete("/{task_id}")
async def delete_task(task_id: UUID, db: Session = Depends(get_db_context)):
    TaskService().delete_task(db, task_id)
