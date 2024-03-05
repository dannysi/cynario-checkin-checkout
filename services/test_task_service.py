from unittest.mock import patch
from services.task_service import TaskService
from entities.task import OngoingTask, FinishedTask


# Mock the TaskDatabase and timedelta_to_words
@patch('services.task_service.task_db')
def test_create_task(mock_task_db):
    owner, name = "user1", "Task 1"
    mock_task_db.add_ongoing_task.return_value = True

    assert TaskService.create_task(owner, name) == True
    call_args = mock_task_db.add_ongoing_task.call_args_list[0][0]
    assert call_args[0] == owner
    assert call_args[1].name == name


@patch('services.task_service.task_db')
def test_finish_task(mock_task_db):
    owner = "user2"
    mock_task_db.has_ongoing_task.return_value = True
    mock_task_db.get_and_delete_ongoing_task.return_value = OngoingTask("Task 2")
    mock_task_db.add_finished_task_to_owner.return_value = True

    assert TaskService.finish_task(owner) == True
    mock_task_db.has_ongoing_task.assert_called_once_with(owner)
    mock_task_db.get_and_delete_ongoing_task.assert_called_once_with(owner)
    mock_task_db.add_finished_task_to_owner.assert_called()

@patch('services.task_service.task_db')
def test_finish_task_fail(mock_task_db):
    owner = "user2"
    assert TaskService.finish_task(owner) == True
    mock_task_db.has_ongoing_task.assert_called_once_with(owner)
    mock_task_db.get_and_delete_ongoing_task.assert_called_once_with(owner)
    mock_task_db.add_finished_task_to_owner.assert_called()


@patch('services.task_service.task_db')
@patch('services.task_service.timedelta_to_words', return_value="1 hour")
def test_report_finished_tasks(mock_timedelta_to_words, mock_task_db):
    mock_task_db.get_all_finished_tasks.return_value = {
        "user3": [FinishedTask(OngoingTask("Task 3"))]
    }
    expected_result = {
        "user3": [{"name": "Task 3", "duration": "1 hour"}]
    }

    assert TaskService.report_finished_tasks() == expected_result
    mock_task_db.get_all_finished_tasks.assert_called_once()