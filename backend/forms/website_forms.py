# -*- coding:utf-8 -*-
from django import forms
#from django.contrib.auth.models import User
from model.website_tb import UserWebsite
from django.conf import settings
User = settings.AUTH_USER_MODEL 
class UserWebsiteDorm(forms.Form):
    class Meta:
        model = UserWebsite
        fields = ('name')

