from datetime import datetime

from django.shortcuts import render
from structlog import get_logger
from tasks.models import Task

logger = get_logger()


def get_task(request, difficulty):
    task = Task.objects.get(week_number=datetime.today().isocalendar()[1], difficulty=difficulty)
    logger.warn(task.as_dict())
    return render(request, "task.html", context=task.as_dict())
