# -*- coding:utf-8 -*-
from django import forms
#from django.contrib.auth.models import User
from .models import Website, WebsitePage, WebsitePanel, WebsiteUrl
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name', 'page_count')

class WebsitePageForm(forms.ModelForm):
    class Meta:
        model = WebsitePage
        fields = ('name', 'page_data', 'order', 'user_id', 'website_id')    

class WebsitePanelForm(forms.ModelForm):
    class Meta:
        model = WebsitePanel
        fields = ('name', 'order', 'user_id', 'website_id', 'website_page_id') 


class WebsiteUrlForm(forms.ModelForm):
    class Meta:
        model = WebsiteUrl
        fields = ('name', 'column', 'line', 'user_id', 'website_id', 'website_page_id', 'website_panel_id') 

