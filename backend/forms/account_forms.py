# -*- coding:utf-8 -*-
from django import forms
from model.account_tb import UserProfile, UserSalt
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)

    class Meta:
        model = User    
        fields = ( "email",)

    def clean_password2(self):    
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("passwords do not match.")
        return data['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname', 'phone_1', 'phone_2', 'qq', 'wechat', 'user_id')

class UserSaltForm(forms.ModelForm):
    class Meta:
        model = UserSalt
        fields = ('salt', 'user_id')