from django.shortcuts import render


def home_page_view(request):
    """
    Renders the home page.

    Args:
        request (WSGIRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template for the home page.

    Usage:
        url_patterns = [
            path('', views.home_page_view, name='home'),
        ]
    """
    return render(request, 'home.html')
