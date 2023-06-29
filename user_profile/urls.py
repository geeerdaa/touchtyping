from django.urls import path
from . import views
from touchtyping import settings
from django.conf.urls.static import static


urlpatterns = [
    path('achievements/', views.achievements, name='achievements'),
    path('stats/', views.stats, name='stats'),
    path('friend/', views.friend, name='friend'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('user_profile/', views.user_profile, name='user_profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
