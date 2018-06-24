# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # 用户名可以是邮箱、英文数字混合、手机号等等，但一定要唯一
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, verbose_name='昵称', unique=True)
    phone_1 = models.CharField(max_length=20, verbose_name='手机号码1')
    phone_2 = models.CharField(max_length=20, verbose_name='手机号码2')
    qq = models.CharField(max_length=20, verbose_name='qq号码')
    wechat = models.CharField(max_length=100, verbose_name='微信号')


    class Meta:
        app_label = 'backend'
        verbose_name = '用户详细信息'
        db_table = 'account_user_profile'
        
    def __str__(self):
        return str(self.nickname)

class UserSalt(models.Model):
    salt = models.CharField(max_length=10, verbose_name='加密用盐值')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'backend'
        verbose_name = '加密用盐值'
        db_table = 'account_user_salt'
        
    def __str__(self):
        return str(self.salt)