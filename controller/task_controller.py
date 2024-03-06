from typing import Optional

from fastapi import APIRouter, HTTPException

from services.task_service import TaskService

router = APIRouter()
task_service = TaskService()


@router.get("/{user}/checkin/{task}")
def checkin(user: str, task: str):
    return "Success" if task_service.create_task(user, task) else "Failed"



@router.get("/{checkout_user}/checkout")
def checkout(checkout_user: str):
    try:
        success = task_service.finish_task(checkout_user)
    except HTTPException as e:
        raise e
    return "Success" if success else "Failed"


@router.get("/report")
def report():
    return task_service.report_finished_tasks()

