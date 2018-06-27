# -*- coding: utf-8 -*-
from functools import wraps
import json
from django.http import HttpResponse
from modules.RESPONSE import CODE_MSG
# Create your views here.


def user_passes_test(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            return HttpResponse(json.dumps(CODE_MSG['permission_check_failed']))
        return _wrapped_view
    return decorator

def auth_check(function=None):
    """
    Decorator for views that checks that the user is logged in.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

