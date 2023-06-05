from django.urls import path, include
from django.views.generic import TemplateView
from login.views import Register

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # TODO: REPLACE WITH NORMAL PROFILE VIEW
]
