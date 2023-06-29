import structlog
from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout, \
    get_user_model
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from login.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


User = get_user_model()
logger = structlog.get_logger()


class Register(View):
    """
    A class-based view for handling user registration.

    Attributes:
        template_name (str): The name of the template to render for the registration page.

    Methods:
        get(request: WSGIRequest) -> HttpResponse:
            Handles HTTP GET requests for the registration page.
            Renders the registration form with a new instance of NewUserForm.
            Returns the rendered template with the form as the context.

        post(request: WSGIRequest) -> HttpResponse:
            Handles HTTP POST requests for the registration page.
            Validates the submitted form data using NewUserForm.
            If the form is valid, saves the user object, authenticates the user, logs them in,
            and redirects them to the home page.
            If the form is invalid, returns the registration form with validation errors as the context.

    Usage:
        view = Register.as_view()
        url_patterns = [
            path('register/', view, name='register'),
        ]
    """
    template_name = 'register.html'

    def get(self, request: WSGIRequest):
        """
        Handles HTTP GET requests for the registration page.

        Args:
            request (WSGIRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered template for the registration page.
        """
        context = {
            'form': NewUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Handles HTTP POST requests for the registration page.

        Args:
            request (WSGIRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered template for the registration page
                with the registration form or a redirection to the home page.
        """
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
    """
    Handles user login authentication.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the login page with the login form
            or a redirection to the home page if the login is successful.

    Usage:
        url_patterns = [
            path('login/', views.login, name='login'),
        ]
    """
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


def profile_page_view(request):
    """
    Renders the profile page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the profile page.

    Usage:
        url_patterns = [
            path('profile/', views.profile_page_view, name='profile'),
        ]
    """
    return render(request, 'profile.html')


def logout_page_view(request):
    """
    Logs out the current user and redirects them to the home page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirection to the home page.

    Usage:
        url_patterns = [
            path('logout/', views.logout_page_view, name='logout'),
        ]
    """
    django_logout(request)
    return redirect(reverse("home"))
