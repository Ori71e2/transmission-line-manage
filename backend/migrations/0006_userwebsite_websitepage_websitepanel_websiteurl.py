# Generated by Django 2.0.6 on 2018-07-21 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0005_auto_20180721_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWebsite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='用户网站名称')),
                ('page_count', models.CharField(max_length=20, verbose_name='网站下属导航页面数量')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_user_website', 'View UserWebsite'), ('change_user_website', 'Change User Website'), ('remove_user_website', 'Remove User Website'), ('delete_user_website', 'Delete User Website')),
                'db_table': 'user_website',
                'verbose_name': '用户收藏网页总览',
            },
        ),
        migrations.CreateModel(
            name='WebsitePage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='页面名称')),
                ('data', models.CharField(max_length=100, verbose_name='json数据')),
                ('order', models.CharField(max_length=10, verbose_name='显示顺序')),
                ('user_website_id', models.UUIDField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_website_page', 'View Website Page'), ('change_website_page', 'Change Website Page'), ('remove_website_page', 'Remove Website Page'), ('delete_website_page', 'Delete Website Page')),
                'db_table': 'website_page',
                'verbose_name': '网站页面',
            },
        ),
        migrations.CreateModel(
            name='WebsitePanel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='导航页中的一栏')),
                ('order', models.CharField(max_length=10, verbose_name='显示顺序')),
                ('user_website_id', models.UUIDField(blank=True, default=None, null=True)),
                ('website_page_id', models.UUIDField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_website_panel', 'View Website Panel'), ('change_website_panel', 'Change Website Panel'), ('remove_website_panel', 'Remove Website Panel'), ('delete_website_panel', 'Delete Website Panel')),
                'db_table': 'website_panel',
                'verbose_name': '导航页中一栏',
            },
        ),
        migrations.CreateModel(
            name='WebsiteUrl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('column', models.CharField(max_length=10, verbose_name='列数')),
                ('line', models.CharField(max_length=10, verbose_name='行数')),
                ('user_website_id', models.UUIDField(blank=True, default=None, null=True)),
                ('website_page_id', models.UUIDField(blank=True, default=None, null=True)),
                ('website_panel_id', models.UUIDField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_website_url', 'View Website Url'), ('change_website_url', 'Change Website Url'), ('remove_website_url', 'Remove Website Url'), ('delete_website_url', 'Delete Website Url')),
                'db_table': 'website_url',
                'verbose_name': '网站url',
            },
        ),
    ]
