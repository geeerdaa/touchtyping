from datetime import datetime

import structlog
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from tasks.models import Task, Score

User = get_user_model()


@login_required(login_url=reverse_lazy("login"))
def get_task_menu(request):
    difficulties = [i[0] for i in Task.objects.values_list("difficulty").distinct()]
    return render(request, "task_menu.html", context={"task_difficulties": difficulties})


@login_required(login_url=reverse_lazy("login"))
def get_task(request, difficulty):
    if not request.user.is_authenticated:
        redirect(reverse('register'))

    task = Task.objects.get(week_number=datetime.today().isocalendar()[1], difficulty=difficulty)

    return render(request, "task.html", context=task.as_dict())


@method_decorator(login_required, name='dispatch')
class Leaderboards(ListView):
    model = Score
    template_name = "leaderboards.html"

    def post(self, request, difficulty):
        time = float(request.POST["time"].split(' ')[0])
        task = Task.objects.get(week_number=datetime.today().isocalendar()[1], difficulty=difficulty)

        user = User.objects.get(username=request.user.username)
        score = Score(
            user=user,
            time=time,
            task=task
        )
        score.update_achievements()
        score.save()

        return redirect(reverse('home'))

    def get_queryset(self):
        return Score.objects.all().order_by("time").filter(task__difficulty=self.kwargs["difficulty"])[:10]

    def __update_achievements(self, score):
        better_scores_amount = Score.objects.all().filter(task__difficulty=self.kwargs["difficulty"], time__lt=score.time).count()
        all_scores_amount = Score.objects.all().filter(task__difficulty=self.kwargs["difficulty"]).count()
