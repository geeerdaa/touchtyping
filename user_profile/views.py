from django.shortcuts import render, redirect
from .forms import ProfileForm, ImageForm


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
    if not request.user.is_authenticated:
        raise Exception('AUTH PLEASE')

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


def user_profile(request):
    if not request.user.is_authenticated:
        raise Exception('AUTH PLEASE')

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'profile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'profile.html', {'form': form})


