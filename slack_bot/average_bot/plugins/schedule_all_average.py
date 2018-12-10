from rtmbot.core import Plugin

from ..jobs import AllAverageJob
from .config import SCHEDULE_TIME


class ScheduleAllAveragePlugin(Plugin):
    def register_jobs(self):
        job = AllAverageJob(SCHEDULE_TIME)
        self.jobs.append(job)
