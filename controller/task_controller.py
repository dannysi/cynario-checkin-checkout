from typing import Optional

from fastapi import APIRouter, HTTPException

from services.task_service import TaskService

router = APIRouter()
task_service = TaskService()


@router.get("/checkin")
def checkin(user: Optional[str] = None, task: Optional[str] = None):
    return "Success" if task_service.create_task(user, task) else "Failed"



@router.get("/checkout")
def checkout(user: Optional[str] = None):
    try:
        success = task_service.finish_task(user)
    except HTTPException as e:
        raise e
    return "Success" if success else "Failed"


@router.get("/report")
def report():
    return task_service.report_finished_tasks()

