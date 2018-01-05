from django import forms
from .models import Email


class EmailForm(forms.Form):
    email = forms.CharField(label='Email', max_length=255)
