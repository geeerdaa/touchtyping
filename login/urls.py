from django.urls import path, include
from django.views.generic import TemplateView
from login.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]
