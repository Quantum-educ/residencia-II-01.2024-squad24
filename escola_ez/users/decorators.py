from django.conf import settings
from django.shortcuts import redirect


def redirect_authenticate(function=None, redirect_url=settings.LOGIN_REDIRECT_URL):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return function(request, *args, **kwargs)
    return wrapper
