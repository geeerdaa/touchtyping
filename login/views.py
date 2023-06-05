from django.contrib.auth import authenticate as django_authenticate, login as django_login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from login.forms import UserCreationForm


class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context ={
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = django_authenticate(username=username, password=password)
            django_login(request, user)
            return redirect(reverse('home'))
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def login(request):
    pass
