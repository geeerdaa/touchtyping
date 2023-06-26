from django.shortcuts import render


def achievements(request):
    return render(request, 'achievements.html')


def stats(request):
    return render(request, 'stats.html')


def friend(request):
    return render(request, 'friend.html')


def profile_settings(request):
    return render(request, 'profile_settings.html')
