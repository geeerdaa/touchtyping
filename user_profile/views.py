from django.shortcuts import render, redirect
from .forms import ProfileForm, ImageForm


def achievements(request):
    return render(request, 'achievements.html')


def stats(request):
    return render(request, 'stats.html')


def friend(request):
    return render(request, 'friend.html')


def profile_settings(request):
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


