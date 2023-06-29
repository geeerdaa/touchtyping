from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    """
    Custom User model that extends Django's AbstractUser.

    Usage:
        - In your Django project's settings.py file, set the AUTH_USER_MODEL to 'your_app.User'.

    Example:
        AUTH_USER_MODEL = 'your_app.User'
    """
    pass
