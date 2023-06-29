from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f'Profile of user { self.user }'
