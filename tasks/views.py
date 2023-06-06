from datetime import datetime

from django.shortcuts import render
from tasks.models import Task


def get_task(request, difficulty):
    task = Task.objects.get(week_number=datetime.today().isocalendar()[1], difficulty=difficulty)
    return render(request, "task.html", context=task.as_dict())
