# Generated by Django 2.0.6 on 2018-07-25 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180724_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户详细信息'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='account_user',
        ),
    ]