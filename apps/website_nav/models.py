# -*- coding:utf-8 -*-
from django.db import models
import uuid

class Website(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='用户网站名称')
    page_count = models.CharField(max_length=20, verbose_name='网站下属导航页面数量')
    user_id = models.UUIDField(default=None, null=True, blank=True)
    class Meta:
        verbose_name = '用户收藏网页总览'
        db_table = 'website'
        permissions = (
            ('view_user_website', 'View UserWebsite'),
            ('change_user_website', 'Change User Website'),
            ('remove_user_website', 'Remove User Website'),
            ('delete_user_website', 'Delete User Website')
        )
        
    def __str__(self):
        return self.name

class WebsitePage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='页面名称')
    page_data = models.CharField(max_length=100, verbose_name='json数据')
    order = models.CharField(max_length=10, verbose_name='显示顺序')
    user_id = models.UUIDField(default=None, null=True, blank=True)
    website_id = models.UUIDField(default=None, null=True, blank=True)

    class Meta:
        verbose_name = '网站页面'
        db_table = 'website_page'
        permissions = (
            ('view_website_page', 'View Website Page'),
            ('change_website_page', 'Change Website Page'),
            ('remove_website_page', 'Remove Website Page'),
            ('delete_website_page', 'Delete Website Page')
        )
        
    def __str__(self):
        return self.name


class WebsitePanel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='导航页中的一栏')
    order = models.CharField(max_length=10, verbose_name='显示顺序')
    user_id = models.UUIDField(default=None, null=True, blank=True)
    website_id = models.UUIDField(default=None, null=True, blank=True)
    website_page_id = models.UUIDField(default=None, null=True, blank=True)
    class Meta:
        verbose_name = '导航页中一栏'
        db_table = 'website_panel'
        permissions = (
            ('view_website_panel', 'View Website Panel'),
            ('change_website_panel', 'Change Website Panel'),
            ('remove_website_panel', 'Remove Website Panel'),
            ('delete_website_panel', 'Delete Website Panel')
        )
        
    def __str__(self):
        return self.name


class WebsiteUrl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=100, verbose_name='')
    column = models.CharField(max_length=10, verbose_name='列数')
    line = models.CharField(max_length=10, verbose_name='行数')
    user_id = models.UUIDField(default=None, null=True, blank=True)
    website_id = models.UUIDField(default=None, null=True, blank=True)
    website_page_id = models.UUIDField(default=None, null=True, blank=True)
    website_panel_id = models.UUIDField(default=None, null=True, blank=True)
    class Meta:
        verbose_name = '网站url'
        db_table = 'website_url'
        permissions = (
            ('view_website_url', 'View Website Url'),
            ('change_website_url', 'Change Website Url'),
            ('remove_website_url', 'Remove Website Url'),
            ('delete_website_url', 'Delete Website Url')
        )
        
    def __str__(self):
        return self.name
