# -*- coding:utf-8 -*-
from django.db import models
#from django.contrib.auth.models import User
import uuid
from django.conf import settings
User = settings.AUTH_USER_MODEL 
class UserProfile(models.Model):
    # 用户名可以是邮箱、英文数字混合、手机号等等，但一定要唯一
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, verbose_name='昵称', unique=True)
    phone_1 = models.CharField(max_length=20, verbose_name='手机号码1')
    phone_2 = models.CharField(max_length=20, verbose_name='手机号码2')
    qq = models.CharField(max_length=20, verbose_name='qq号码')
    wechat = models.CharField(max_length=100, verbose_name='微信号')


    class Meta:
        app_label = 'backend'
        verbose_name = '用户详细信息'
        db_table = 'account_user_profile'
        permissions = (
            ('view_user_profile', 'View UserProfile'),
            ('change_user_profile', 'Change User Profile'),
            ('remove_user_profile', 'Remove User Profile'),
            ('delete_user_profile', 'Delete User Profile')
        )
        
    def __str__(self):
        return str(self.nickname)

class UserSalt(models.Model):
    salt = models.CharField(max_length=10, verbose_name='加密用盐值')
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'backend'
        verbose_name = '加密用盐值'
        db_table = 'account_user_salt'
        permissions = (
            ('view_salt', 'View Salt'),
            ('change_salt', 'Change Salt'),
            ('remove_salt', 'Remove Salt'),
            ('delete_salt', 'Delete Salt')
        )
        
    def __str__(self):
        return str(self.salt)
"""
class UserWebsite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='用户网站名称', unique=True)
    page_count = models.CharField(max_length=20, verbose_name='网站下属导航页面数量')

    class Meta:
        app_label = 'backend'
        verbose_name = '用户收藏网页总览'
        db_table = 'user_website'
        permissions = (
            ('view_user_website', 'View UserWebsite'),
            ('change_user_website', 'Change User Website'),
            ('remove_user_website', 'Remove User Website'),
            ('delete_user_website', 'Delete User Website')
        )
        
    def __str__(self):
        return str(self.name)

class WebsitePage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='页面名称')
    data = models.CharField(max_length=100, verbose_name='json数据')
    order = models.CharField(max_length=10, verbose_name='显示顺序')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_website_id = models.UUIDField(default=None, null=True, blank=True)

    class Meta:
        app_label = 'backend'
        verbose_name = '网站页面'
        db_table = 'website_page'
        permissions = (
            ('view_website_page', 'View Website Page'),
            ('change_website_page', 'Change Website Page'),
            ('remove_website_page', 'Remove Website Page'),
            ('delete_website_page', 'Delete Website Page')
        )
        
    def __str__(self):
        return str(self.name)


class WebsitePanel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='导航页中的一栏')
    order = models.CharField(max_length=10, verbose_name='显示顺序')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_website_id = models.UUIDField(default=None, null=True, blank=True)
    website_page_id = models.UUIDField(default=None, null=True, blank=True)
    class Meta:
        app_label = 'backend'
        verbose_name = '导航页中一栏'
        db_table = 'website_panel'
        permissions = (
            ('view_website_panel', 'View Website Panel'),
            ('change_website_panel', 'Change Website Panel'),
            ('remove_website_panel', 'Remove Website Panel'),
            ('delete_website_panel', 'Delete Website Panel')
        )
        
    def __str__(self):
        return str(self.name)


class WebsiteUrl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='')
    column = models.CharField(max_length=10, verbose_name='列数')
    line = models.CharField(max_length=10, verbose_name='行数')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_website_id = models.UUIDField(default=None, null=True, blank=True)
    website_page_id = models.UUIDField(default=None, null=True, blank=True)
    website_panel_id = models.UUIDField(default=None, null=True, blank=True)
    class Meta:
        app_label = 'backend'
        verbose_name = '网站url'
        db_table = 'website_url'
        permissions = (
            ('view_website_url', 'View Website Url'),
            ('change_website_url', 'Change Website Url'),
            ('remove_website_url', 'Remove Website Url'),
            ('delete_website_url', 'Delete Website Url')
        )
        
    def __str__(self):
        return str(self.name)
"""