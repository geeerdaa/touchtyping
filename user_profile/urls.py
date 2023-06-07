from django.urls import path
from . import views


urlpatterns = [
    path('achievements/', views.achievements, name='achievements'),
    path('stats/', views.stats, name='stats'),
    path('friend/', views.friend, name='friend'),
    path('profile_settings/', views.profile_settings, name='profile_settings')
]
