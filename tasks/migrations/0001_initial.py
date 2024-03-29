# Generated by Django 4.2.1 on 2023-06-25 16:05
from datetime import datetime

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db.migrations import RunPython


def create_default_entries(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    for week_number in range(52):
        for difficulty in range(10):
            Task.objects.create(
                content=f"{difficulty:02}d {week_number:02}w ff gg ss",
                difficulty=difficulty,
                week_number=week_number
            ).save()

    Achievement = apps.get_model('tasks', 'Achievement')
    AchievementCriterion = apps.get_model('tasks', 'AchievementCriterion')
    User = apps.get_model('login', 'User')
    users = [User.objects.get(username="berdnikovEV"), ]

    achievements_list = [
        {
            "name": "First Success",
            "description": "Finish a task",
            "criterion_type": "complete_tasks",
            "criterion_value": 1
        },
        {
            "name": "Unstoppable",
            "description": "Finish every task at least once",
            "criterion_type": "complete_tasks",
            "criterion_value": -1
        },
        {
            "name": "Top 50%",
            "description": "Beat 50% of players at any task",
            "criterion_type": "top_score_percent",
            "criterion_value": 50
        },
        {
            "name": "Top 25%",
            "description": "Beat 75% of players at any task",
            "criterion_type": "top_score_percent",
            "criterion_value": 25
        },
        {
            "name": "Top 10%",
            "description": "Beat 90% of players at any task",
            "criterion_type": "top_score_percent",
            "criterion_value": 10
        },
        {
            "name": "Top 5%",
            "description": "Beat 95% of players at any task",
            "criterion_type": "top_score_percent",
            "criterion_value": 5
        },
        {
            "name": "Top 50",
            "description": "Become one of the 50 best players at any task",
            "criterion_type": "top_n_score",
            "criterion_value": 50
        },
        {
            "name": "Top 10",
            "description": "Become one of the 10 best players at any task",
            "criterion_type": "top_n_score",
            "criterion_value": 10
        },
        {
            "name": "Top 1",
            "description": "Become THE BEST at any task",
            "criterion_type": "top_n_score",
            "criterion_value": 1
        },
    ]

    for achievement_data in achievements_list:
        achievement_criterion = AchievementCriterion(
            criterion_type=achievement_data["criterion_type"],
            criterion_value=achievement_data["criterion_value"],
        )
        achievement_criterion.save()

        achievement = Achievement.objects.create(
            name=achievement_data["name"],
            description=achievement_data["description"],
            achievement_criterion=achievement_criterion,
        )
        achievement.users.set(users)
        achievement.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementCriterion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterion_type', models.CharField(choices=[('top_n_score', 'Top n Score'), ('top_score_percent', 'Top n% Score'), ('complete_all_tasks', 'Complete N Tasks')], max_length=100)),
                ('criterion_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30)),
                ('difficulty', models.CharField(max_length=30)),
                ('week_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('achievement_criterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criterion', to='tasks.achievementcriterion')),
                ('users', models.ManyToManyField(related_name='achievements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        RunPython(create_default_entries)
    ]
