from django.shortcuts import render


def achievements(request):
    """
    Renders the achievements page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the achievements page.

    Usage:
        url_patterns = [
            path('achievements/', views.achievements, name='achievements'),
        ]
    """
    return render(request, 'achievements.html')


def stats(request):
    """
    Renders the stats page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the stats page.

    Usage:
        url_patterns = [
            path('stats/', views.stats, name='stats'),
        ]
    """
    return render(request, 'stats.html')


def friend(request):
    """
    Renders the friend page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the friend page.

    Usage:
        url_patterns = [
            path('friend/', views.friend, name='friend'),
        ]
    """
    return render(request, 'friend.html')


def profile_settings(request):
    """
    Renders the profile settings page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the profile settings page.

    Usage:
        url_patterns = [
            path('profile/settings/', views.profile_settings, name='profile_settings'),
        ]
    """
    return render(request, 'profile_settings.html')
