from django.apps import AppConfig


class WebsiteNavConfig(AppConfig):
    name = 'website_nav'
    def ready(self):
        import website_nav.signals 