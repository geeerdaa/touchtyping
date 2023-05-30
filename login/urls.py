from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('home_page', TemplateView.as_view(template_name='home.html'), name='profile'),  # TODO: REPLACE WITH NORMAL PROFILE VIEW
]