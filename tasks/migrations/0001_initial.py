# Generated by Django 4.2.1 on 2023-06-25 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db.migrations import RunPython
from touchtyping.constants import achievements_list, task_by_difficulty


def create_default_entries(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    for difficulty, task_by_week in enumerate(task_by_difficulty):
        for week_number, task in enumerate(task_by_week):
            Task.objects.create(
                content=task,
                difficulty=difficulty,
                week_number=week_number
            ).save()

    Achievement = apps.get_model('tasks', 'Achievement')
    AchievementCriterion = apps.get_model('tasks', 'AchievementCriterion')
    User = apps.get_model('login', 'User')
    users = [
        User.objects.get(username="berdnikovEV"),
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
