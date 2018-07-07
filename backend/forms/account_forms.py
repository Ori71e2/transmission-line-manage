# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from models.account_tb import UserProfile, UserSalt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)

    class Meta:
        model = User    
        fields = ("username", "email")

    def clean_password2(self):    
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("passwords do not match.")
        return data['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname', 'phone_1', 'phone_2', 'qq', 'wechat')

class UserSaltForm(forms.ModelForm):
    class Meta:
        model = UserSalt
        fields = ('salt',)