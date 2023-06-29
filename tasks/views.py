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
    """
    Renders the task menu page with a list of task difficulties.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the task menu page.

    Usage:
        url_patterns = [
            path('task/menu/', views.get_task_menu, name='task_menu'),
        ]
    """
    difficulties = [i[0] for i in Task.objects.values_list("difficulty").distinct()]
    return render(request, "task_menu.html", context={"task_difficulties": difficulties})


@login_required(login_url=reverse_lazy("login"))
def get_task(request, difficulty):
    """
    Renders the task page for the specified difficulty.

    Args:
        request (WSGIRequest): The HTTP request object.
        difficulty (str): The difficulty level of the task.

    Returns:
        HttpResponse: The rendered template for the task page.

    Usage:
        url_patterns = [
            path('task/<str:difficulty>/', views.get_task, name='task'),
        ]
    """
    if not request.user.is_authenticated:
        redirect(reverse('register'))

    task = Task.objects.get(week_number=datetime.today().isocalendar()[1], difficulty=difficulty)

    return render(request, "task.html", context=task.as_dict())


@method_decorator(login_required, name='dispatch')
class Leaderboards(ListView):
    """
    Displays the leaderboards for a specific task difficulty.

    Attributes:
        model (Score): The model used for retrieving scores.
        template_name (str): The name of the template to render for the leaderboards page.

    Methods:
        post(request, difficulty):
            Handles HTTP POST requests for submitting a score.
            Creates a new score object and updates the user's achievements.
            Redirects to the home page.

        get_queryset(self):
            Retrieves the queryset of scores for the specific task difficulty.

        __update_achievements(self, score):
            Updates the achievements for the given score.

    Usage:
        view = Leaderboards.as_view()
        url_patterns = [
            path('leaderboards/<str:difficulty>/', view, name='leaderboards'),
        ]
    """
    model = Score
    template_name = "leaderboards.html"

    def post(self, request, difficulty):
        """
        Handles HTTP POST requests for submitting a score.

        Args:
            request (WSGIRequest): The HTTP request object.
            difficulty (str): The difficulty level of the task.

        Returns:
            HttpResponse: A redirection to the home page.

        """
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
        """
        Retrieves the queryset of scores for the specific task difficulty.

        Returns:
            QuerySet: The queryset of scores ordered by time and filtered by task difficulty.
        """
        return Score.objects.all().order_by("time").filter(task__difficulty=self.kwargs["difficulty"])[:10]

    def __update_achievements(self, score):
        """
        Updates the achievements for the given score.

        Args:
            score: The score object for which the achievements need to be updated.
        """
        better_scores_amount = Score.objects.all().filter(task__difficulty=self.kwargs["difficulty"], time__lt=score.time).count()
        all_scores_amount = Score.objects.all().filter(task__difficulty=self.kwargs["difficulty"]).count()
