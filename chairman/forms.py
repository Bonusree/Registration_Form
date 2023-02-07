from django import forms
from django.utils.safestring import mark_safe

class cman(forms.Form):
    Email=forms.EmailField(label='email', max_length=250)
    Password=forms.CharField(label='Password', widget=forms.PasswordInput, max_length=250)