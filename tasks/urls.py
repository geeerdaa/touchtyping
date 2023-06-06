from django.urls import path

from .views import get_task

urlpatterns = [
    path('<int:difficulty>', get_task),
]