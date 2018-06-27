# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from forms.account_forms import LoginForm
from modules.RESPONSE import CODE_MSG
import json
@method_decorator(sensitive_post_parameters())
@method_decorator(csrf_protect)
@method_decorator(never_cache)
def login(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        login_data = login_form.clean_data
        username = login_data['username']
        password = login_data['password']
        user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth_login(request, user)
        return HttpResponse(json.dumps(CODE_MSG['success']))
    else:
        return HttpResponse(json.dumps(CODE_MSG['login_failed'])


def logout(request):
    auth_logout(request)
    return HttpResponse(json.dumps(CODE_MSG['success']))

