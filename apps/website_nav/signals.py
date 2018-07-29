# -*- coding:utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()
from website_nav.models import Website, WebsitePage, WebsitePanel, WebsiteUrl

@receiver(post_save, sender=User)
def create_user_website(sender, instance, created, **kwargs):
    if created:
        Website.objects.create(user_id=instance.id)



