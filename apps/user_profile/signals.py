# -*- coding:utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.apps import apps

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("Website Nav Signals")
    if created:
        print("created")
        UserProfile = apps.get_model("user_profile","UserProfile")
        print(instance.id)
        UserProfile.objects.create(user_id=instance.id)
    


