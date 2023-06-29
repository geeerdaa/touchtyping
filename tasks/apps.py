from django.apps import AppConfig


class TasksConfig(AppConfig):
    """
    Django application configuration for the 'tasks' app.

    This class represents the configuration for the 'tasks' app in a Django project. It inherits from Django's
    AppConfig class and provides additional settings specific to the 'tasks' app.

    Attributes:
        default_auto_field (str): The default auto-generated field for models in the app.
        name (str): The name of the app.

    Usage:
        - In the Django project's settings.py file, add 'tasks' to the list of installed apps:

            ```
            INSTALLED_APPS = [
                ...
                'tasks',
                ...
            ]
            ```

    Example:
        ```
        class TasksConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'tasks'
        ```
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
