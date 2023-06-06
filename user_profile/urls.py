from django.urls import path
from . import views


urlpatterns = [
    path('achievements/', views.achievements, name='achievements'),
    path('stats/', views.stats, name='stats'),
    path('friend/', views.stats, name='friend'),
]
