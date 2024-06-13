from django import forms
from django.contrib.auth.models import User

class regForm(forms.Form):
    username = forms.CharField (max_length=100)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)