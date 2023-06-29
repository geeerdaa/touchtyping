from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout, \
    get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from login.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


User = get_user_model()


class Register(View):

    template_name = 'register.html'

    def get(self, request):
        context = {
            'form': NewUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = django_authenticate(username=username, password=password)
            django_login(request, user)
            return redirect(reverse('home'))
        context = {
            'error_list': str(form.errors),
            'form': form,
        }
        return render(request, self.template_name, context)


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = django_authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect(reverse("home"))
    context = {
        'error_list': str(form.errors),
        "login_form": form
    }
    return render(request, template_name="login.html", context=context)


def second_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = django_authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect(reverse("home"))
    context = {
        'error_list': str(form.errors),
        "login_form": form
    }
    return render(request, template_name="login_for_redirect.html", context=context)


def logout_page_view(request):
    django_logout(request)
    return redirect(reverse("home"))
