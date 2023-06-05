from tasks.models import Task

for week_number in range(52):
    for difficulty in range(10):
        task = Task(
            content=f"{difficulty:02}d {week_number:02}w ff gg ss",
            difficulty=difficulty,
            week_number=week_number
        )
        task.save()
