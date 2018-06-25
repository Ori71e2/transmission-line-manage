"""pyhacker URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path,re_path, include
from django.views.generic import TemplateView  
from modules.account import (register, get_user_profile, set_user_profile, login, logout)

urlpatterns = [
    # 一级路径必须带/结尾
    re_path(r'^account/$', TemplateView.as_view(template_name="index.html")),
    re_path(r'^account/register$', register),
    re_path(r'^account/get_user_profile$', get_user_profile),
    re_path(r'^account/set_user_profile$', set_user_profile),
    re_path(r'^account/login$', login),
    re_path(r'^account/logout$', logout),
]


