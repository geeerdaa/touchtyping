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

    def update_achievements(self):
        for achievement in Achievement.objects.all():
            if self.user not in achievement.users.all() and achievement.is_achieved(self):
                achievement.users.add(self.user.id)

    def __repr__(self) -> str:
        return f"{self.user.username or '<empty name>'}: {self.time} s"

    def __str__(self) -> str:
        return f"{self.user.username or '<empty name>'}: {self.time} s"


class AchievementCriterion(models.Model):
    CRITERION_TYPES = [
        ('top_n_score', 'Top n Score'),
        ('top_score_percent', 'Top n% Score'),
        ('complete_all_tasks', 'Complete N Tasks'),
    ]

    criterion_type = models.CharField(max_length=100, choices=CRITERION_TYPES)
    criterion_value = models.IntegerField()

    def is_achieved(self, score):
        """
        Check if the specific achievement criterion is met by the given user.
        """

        if self.criterion_type == 'top_n_score':
            try:
                top_score = Score.objects.filter(user=score.user, task=score.task).order_by('time')\
                    .all()[self.criterion_value]
            except IndexError:
                return False
            else:
                if top_score and score.time <= top_score.time:
                    return True

        if self.criterion_type == 'top_score_percent':
            try:
                top_n_percent_count = round(Score.objects.filter(user=score.user, task=score.task).all().count()
                                            * (self.criterion_value/100))
                top_score = Score.objects.filter(user=score.user, task=score.task).order_by('time')\
                    .all()[top_n_percent_count]
            except IndexError:
                return False
            else:
                if top_score and score.time <= top_score.time:
                    return True

        elif self.criterion_type == 'complete_tasks':
            task_count = Task.objects.filter(week_number=score.task.week_number).count() \
                if self.criterion_value == -1 else self.criterion_value
            user_completed_task_count = Score.objects.filter(user=score.user).values('task').distinct().count()
            if user_completed_task_count >= task_count:
                return True

        return False


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='achievements')
    achievement_criterion = models.ForeignKey(AchievementCriterion, on_delete=models.CASCADE, related_name='criterion')

    def __str__(self):
        return self.name

    def is_achieved(self, user):
        """
        Check if the achievement criteria are met by the given user.
        """
        return self.achievement_criterion.is_achieved(user)
