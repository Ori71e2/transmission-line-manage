from django.urls import path, re_path, include
from django.contrib import admin
from .modules import (register, login, logout, get_csrf_token)

urlpatterns = [
    path('', register),
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('get_csrf_token', get_csrf_token)
]