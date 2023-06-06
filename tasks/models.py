from django.db import models

from login.models import User


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

    task_id = models.IntegerField()
    time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"{self.user.name or '<empty name>'}: {self.time} s"

    def __str__(self) -> str:
        return f"{self.user.name or '<empty name>'}: {self.time} s"
