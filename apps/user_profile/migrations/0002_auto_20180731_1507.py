# Generated by Django 2.0.6 on 2018-07-31 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.UUIDField(blank=True, default=None, null=True, unique=True, verbose_name='用户信息表'),
        ),
    ]