from fastapi import HTTPException

from database.task_db import TaskDatabase
from entities.task import OngoingTask, FinishedTask
from services.utils import timedelta_to_str

task_db = TaskDatabase()


class TaskService(object):

    @staticmethod
    def create_task(owner, name):
        if task_db.has_ongoing_task(owner):
            raise HTTPException(status_code=404, detail="User already has an open task.")
        return task_db.add_ongoing_task(owner, OngoingTask(name))

    @staticmethod
    def finish_task(owner):
        if not task_db.has_ongoing_task(owner):
            raise HTTPException(status_code=404, detail="Task not found for the user.")
        task_db.add_finished_task_to_owner(owner, FinishedTask(task_db.get_and_delete_ongoing_task(owner)))
        return True

    @staticmethod
    def report_finished_tasks():
        answer = {}
        for owner, tasks in task_db.get_all_finished_tasks().items():
            answer[owner] = [{"name": task.name, "duration": timedelta_to_str(task.duration)} for task in tasks]
        return answer
