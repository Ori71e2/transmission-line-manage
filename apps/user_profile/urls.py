from django.urls import path, re_path, include
from django.contrib import admin
from .modules import (get_user_profile, set_user_profile)

urlpatterns = [
    re_path(r'^$', get_user_profile),
    re_path(r'^get_user_profile$', get_user_profile),
    re_path(r'^set_user_profile$', set_user_profile),
]