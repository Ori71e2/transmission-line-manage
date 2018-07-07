from django.shortcuts import render
from django.http import JsonResponse
from forms.account_forms import RegistrationForm, UserProfileForm,UserSaltForm
from models.account_tb import UserProfile, UserSalt
from modules.RESPONSE import CODE_MSG
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
            return JsonResponse(CODE_MSG['success'])
        else: 
            return JsonResponse(CODE_MSG['register_failed'])
    else:
        return JsonResponse(CODE_MSG['register_failed'])
