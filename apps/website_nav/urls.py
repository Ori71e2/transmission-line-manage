from django.urls import path, re_path, include
from django.contrib import admin
from .modules import (get_user_profile, set_user_profile)

urlpatterns = [
    path('', get_user_profile),
    path('get_user_profile', get_user_profile),
    path('set_user_profile', set_user_profile),
]