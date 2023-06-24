from django.db import models

from touchtyping import settings


class Task(models.Model):
    content = models.CharField(max_length=30)
    difficulty = models.CharField(max_length=30)
    week_number = models.IntegerField()

    def as_dict(self):
        return {
            "content": self.content,
            "difficulty": self.difficulty,
            "week_number": self.week_number
        }


class Score(models.Model):
    __tablename__ = "score"

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"{self.user.username or '<empty name>'}: {self.time} s"

    def __str__(self) -> str:
        return f"{self.user.username or '<empty name>'}: {self.time} s"


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_achieved = models.DateField(auto_now_add=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='achievements')

    def __str__(self):
        return self.name
