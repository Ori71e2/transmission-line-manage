from django import forms
from django.contrib.auth.models import User
from models import account

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)

    class Meta:
        model = User    
        fields = ("username", "email")

    def clean_password2(self):    
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("passwords do not match.")
        return data['password2']