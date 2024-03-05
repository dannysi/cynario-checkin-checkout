from collections import defaultdict
from typing import List, Dict

from entities.task import FinishedTask


class TaskDatabase(object):
    ongoing_tasks = {}
    finished_tasks = defaultdict(list)

    def add_ongoing_task(self, owner, ongoing_task):
        self.ongoing_tasks[owner] = ongoing_task
        return True

    def get_and_delete_ongoing_task(self, owner):
        task = self.ongoing_tasks[owner]
        del self.ongoing_tasks[owner]
        return task

    def has_ongoing_task(self, owner):
        return owner in self.ongoing_tasks

    def add_finished_task_to_owner(self, owner, finished_task):
        self.finished_tasks[owner].append(finished_task)
        return True

    def get_all_finished_tasks(self) -> Dict[str, List[FinishedTask]]:
        return self.finished_tasks


