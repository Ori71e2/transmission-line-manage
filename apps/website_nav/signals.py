# -*- coding:utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.apps import apps

#from django.contrib.auth import get_user_model
#User = get_user_model()
#from website_nav.models import Website
#import  apps   
#Website = apps.get_model("WebsiteNavConfig","Website")
#@receiver(post_save, sender=User)
def create_user_website(sender, instance, created, **kwargs):
    print("Website Nav Signals")
    if created:
        print("created")
        Website = apps.get_model("website_nav","Website")
        print(instance.id)
        Website.objects.create(user_id=instance.id)
    


