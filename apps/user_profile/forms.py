# -*- coding:utf-8 -*-
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname', 'phone_1', 'phone_2', 'qq', 'wechat', 'user_id')