# -*- coding:utf-8 -*-
from django.db import models
import uuid

class UserProfile(models.Model):
    # 用户名可以是邮箱、英文数字混合、手机号等等，但一定要唯一
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    nickname = models.CharField(max_length=100, verbose_name='昵称')
    phone_1 = models.CharField(max_length=20, verbose_name='手机号码1')
    phone_2 = models.CharField(max_length=20, verbose_name='手机号码2')
    qq = models.CharField(max_length=20, verbose_name='qq号码')
    wechat = models.CharField(max_length=100, verbose_name='微信号')
    user_id = models.UUIDField(default=None, null=True, blank=True, verbose_name='用户信息表')

    class Meta:
        verbose_name = '用户详细信息'
        db_table = 'auth_user_profile'
        permissions = (
            ('view_user_profile', 'View UserProfile'),
            ('change_user_profile', 'Change User Profile'),
            ('remove_user_profile', 'Remove User Profile'),
            ('delete_user_profile', 'Delete User Profile')
        )
        
    def __str__(self):
        return self.nickname
