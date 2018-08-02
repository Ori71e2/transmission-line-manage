from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from website_nav.signals import create_user_website

class WebsiteNavConfig(AppConfig):
    name = 'website_nav'
    def ready(self):
        User = get_user_model()
        post_save.connect(create_user_website, sender=User)
