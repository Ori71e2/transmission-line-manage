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
