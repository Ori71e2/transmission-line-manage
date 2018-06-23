from django.shortcuts import render
from django.http import HttpResponse
from . forms import LoginForm, RegistrationForm
# Create your views here.
def register(request) :
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False);
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse(True)
        else: 
            return HttpResponse(False)
    else:
        return HttpResponse(False)
