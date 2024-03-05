import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from unittest.mock import patch
from controller.task_controller import router
from services.task_service import TaskService

# Create a test client using the router from task_controller
client = TestClient(router)

def test_checkin_success():
    # Patch the create_task method of TaskService
    with patch.object(TaskService, 'create_task', return_value=True) as mock_create_task:
        response = client.get("/checkin?user=johndoe&task=Task+1")
        assert response.status_code == 200
        assert response.json() == "Success"
        mock_create_task.assert_called_once_with("johndoe", "Task 1")

def test_checkin_failure():
    # Patch the create_task method of TaskService
    with patch.object(TaskService, 'create_task', return_value=False) as mock_create_task:
        response = client.get("/checkin?user=johndoe&task=Task+1")
        assert response.status_code == 200
        assert response.json() == "Failed"
        mock_create_task.assert_called_once_with("johndoe", "Task 1")

def test_checkout_success():
    # Patch the finish_task method of TaskService
    with patch.object(TaskService, 'finish_task', return_value=True) as mock_finish_task:
        response = client.get("/checkout?user=johndoe")
        assert response.status_code == 200
        assert response.json() == "Success"
        mock_finish_task.assert_called_once_with("johndoe")


@patch('services.task_service.task_db')
def test_finish_task_no_ongoing(mock_task_db):
    owner = "user2"
    mock_task_db.has_ongoing_task.return_value = False

    with pytest.raises(HTTPException) as exc_info:
        TaskService.finish_task(owner)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Task not found for the user."
    mock_task_db.has_ongoing_task.assert_called_once_with(owner)
    mock_task_db.get_and_delete_ongoing_task.assert_not_called()
    mock_task_db.add_finished_task_to_owner.assert_not_called()

def test_report():
    # Patch the report_finished_tasks method of TaskService
    with patch.object(TaskService, 'report_finished_tasks', return_value={'task_report': 'some_data'}) as mock_report:
        response = client.get("/report")
        assert response.status_code == 200
        assert response.json() == {'task_report': 'some_data'}
        mock_report.assert_called_once()