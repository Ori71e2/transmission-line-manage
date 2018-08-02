# -*- coding:utf-8 -*-
from django import forms
#from django.contrib.auth.models import User
from .models import Website, WebsitePage, WebsitePanel, WebsiteUrl
class WebsiteForm(forms.Form):
    class Meta:
        model = Website
        fields = ('name', 'page_count','user_id')

class WebsitePageForm(forms.Form):
    class Meta:
        model = Website
        fields = ('name', 'page_data', 'order', 'user_id', 'website_id')    

class WebsitePanelForm(forms.Form):
    class Meta:
        model = WebsitePanel
        fields = ('name', 'order', 'user_id', 'website_id', 'website_page_id') 


class WebsiteUrlForm(forms.Form):
    class Meta:
        model = Website
        fields = ('name', 'column', 'line', 'user_id', 'website_id', 'website_page_id', 'website_panel_id') 

