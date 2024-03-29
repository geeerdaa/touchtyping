from django.urls import path
from login.views import Register
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', views.logout_page_view, name='logout'),
]
