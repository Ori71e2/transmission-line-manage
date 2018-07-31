from django.apps import AppConfig
from django.db.models.signals import post_save

from website_nav.signals import create_user_website

class WebsiteNavConfig(AppConfig):
    name = 'website_nav'
    def ready(self):
        from .import signals