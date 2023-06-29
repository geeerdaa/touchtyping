from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ProfileForm


@login_required(login_url=reverse_lazy("login"))
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


@login_required(login_url=reverse_lazy("login"))
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


@login_required(login_url=reverse_lazy("login"))
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


@login_required(login_url=reverse_lazy("login"))
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
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect('user_profile')
    context = {
        'form': form,
    }
    return render(request, 'profile_settings.html', context)


@login_required(login_url=reverse_lazy("login"))
def user_profile(request):
    """
    Handle a GET or POST request to display and update the user's profile.

    Args:
        request (HttpRequest): The HTTP request object containing metadata and data about the request.

    Raises:
        Exception: If the user is not authenticated.

    Returns:
        HttpResponse: The HTTP response object with the rendered 'profile.html' template.

    """

    return render(request, 'profile.html')


