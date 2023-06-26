from django.urls import path

from .views import get_task, get_task_menu, Leaderboards

urlpatterns = [
    path('', get_task_menu, name="task_menu"),
    path('<int:difficulty>/leaderboards', Leaderboards.as_view(), name="leaderboards"),
    path('<int:difficulty>', get_task, name="task"),
]
