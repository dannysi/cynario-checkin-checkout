import pytest

from database.task_db import TaskDatabase
from entities.task import OngoingTask, FinishedTask


@pytest.fixture
def task_db():
    return TaskDatabase()

def test_add_ongoing_task(task_db):
    owner = "user1"
    task = OngoingTask("Test Task")
    assert not task_db.has_ongoing_task(owner)
    task_db.add_ongoing_task(owner, task)
    assert task_db.has_ongoing_task(owner)

def test_get_and_delete_ongoing_task(task_db):
    owner = "user2"
    task = OngoingTask("Another Task")
    task_db.add_ongoing_task(owner, task)
    fetched_task = task_db.get_and_delete_ongoing_task(owner)
    assert fetched_task == task
    assert not task_db.has_ongoing_task(owner)

def test_has_ongoing_task(task_db):
    owner = "user3"
    assert not task_db.has_ongoing_task(owner)
    task_db.add_ongoing_task(owner, OngoingTask("Some Task"))
    assert task_db.has_ongoing_task(owner)

def test_add_finished_task_to_owner(task_db):
    owner = "user4"
    finished_task = FinishedTask(OngoingTask("Completed Task"))
    task_db.add_finished_task_to_owner(owner, finished_task)
    assert len(task_db.finished_tasks[owner]) == 1
    assert task_db.finished_tasks[owner][0] == finished_task

def test_get_all_finished_tasks(task_db):
    owners_tasks = {
        "user5": [FinishedTask(OngoingTask("Task 5"))],
        "user6": [FinishedTask(OngoingTask("Task 6a")), FinishedTask(OngoingTask("Task 6b"))]
    }
    for owner, tasks in owners_tasks.items():
        for task in tasks:
            task_db.add_finished_task_to_owner(owner, task)

    all_finished = task_db.get_all_finished_tasks()
    assert all(isinstance(tasks, list) for tasks in all_finished.values())
    assert 2 == len(owners_tasks)
    for owner in owners_tasks:
        assert all(task in all_finished[owner] for task in owners_tasks[owner])
