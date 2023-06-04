from django.urls import path, include
from django.views.generic import TemplateView
from login.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('home_page', TemplateView.as_view(template_name='home.html'), name='profile'),  # TODO: REPLACE WITH NORMAL PROFILE VIEW
]