# Create your views here.
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from forms.account_forms import LoginForm
from modules.RESPONSE import CODE_MSG
import json
from django.shortcuts import render
from django.http import JsonResponse
from forms.account_forms import RegistrationForm, UserProfileForm,UserSaltForm
from model.account_tb import UserProfile, UserSalt
from modules.RESPONSE import CODE_MSG
from guardian.shortcuts import assign_perm
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def register(request) :
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False);
            new_user.set_password(user_form.cleaned_data['password'])
            if new_user.save() == 0:
                print('failed')
            #print (new_user.id)
            new_user_profile = UserProfile.objects.create(user_id=new_user.id)
            new_user_salt = UserSalt.objects.create(user_id=new_user.id)
            #assign_perm('view_user_profile', new_user, new_user_profile)
            #assign_perm('change_user_profile', new_user, new_user_profile)
            #assign_perm('view_salt', new_user, new_user_salt)
            return JsonResponse(CODE_MSG['success'])
        else: 
            return JsonResponse(CODE_MSG['register_failed'])
    else:
        return JsonResponse(CODE_MSG['register_failed'])

def login(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        login_data = login_form.cleaned_data
        email = login_data['email']
        password = login_data['password']
        user = authenticate(email=email, password=password)
    if user is not None and user.is_active:
        auth_login(request, user)
        return JsonResponse(CODE_MSG['success'])
    else:
        return JsonResponse(CODE_MSG['login_failed'])


def logout(request):
    auth_logout(request)
    return JsonResponse(CODE_MSG['success'])