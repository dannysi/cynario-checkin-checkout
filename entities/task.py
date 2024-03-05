from datetime import datetime, timedelta


class Task(object):
    name: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)


class OngoingTask(Task):
    start_time: datetime

    def __init__(self, name):
        super().__init__(name)
        self.start_time = datetime.utcnow()


class FinishedTask(Task):
    duration: timedelta

    def __init__(self, ongoing_task: OngoingTask):
        super().__init__(ongoing_task.name)
        self.duration = datetime.utcnow() - ongoing_task.start_time
