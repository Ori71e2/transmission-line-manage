from django.shortcuts import render
from django.http import HttpResponse
from forms.account_forms import RegistrationForm, UserProfileForm,UserSaltForm
from models.account_tb import UserProfile, UserSalt
from modules.RESPONSE import CODE_MSG
import json
# Create your views here.
def register(request) :
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False);
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            UserSalt.objects.create(user=new_user)
            return HttpResponse(json.dumps(CODE_MSG['success']))
        else: 
            return HttpResponse(json.dumps(CODE_MSG['success']))
    else:
        return HttpResponse(json.dumps(CODE_MSG['success']))
