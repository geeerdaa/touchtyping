from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """
    Django application configuration for the 'user_profile' app.

    This class represents the configuration for the 'user_profile' app in a Django project. It inherits from Django's
    AppConfig class and provides additional settings specific to the 'user_profile' app.

    Attributes:
        default_auto_field (str): The default auto-generated field for models in the app.
        name (str): The name of the app.

    Usage:
        - In the Django project's settings.py file, add 'user_profile' to the list of installed apps:

            ```
            INSTALLED_APPS = [
                ...
                'user_profile',
                ...
            ]
            ```

    Example:
        ```
        class UserProfileConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'user_profile'
        ```
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
