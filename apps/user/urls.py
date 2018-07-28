from django.urls import path, re_path, include
from django.contrib import admin
from .modules import (register, login, logout, get_csrf_token)

urlpatterns = [
    re_path(r'^$', register),
    re_path(r'^register$', register),
    re_path(r'^login$', login),
    re_path(r'^logout$', logout),
    re_path(r'^get_csrf_token$', get_csrf_token)
]