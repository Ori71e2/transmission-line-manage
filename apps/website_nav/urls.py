from django.urls import path, re_path, include
from django.contrib import admin
from .modules import (get_website, set_website)

urlpatterns = [
    path('', get_website),
    path('get_website', get_website),
    path('set_website', set_website),
]