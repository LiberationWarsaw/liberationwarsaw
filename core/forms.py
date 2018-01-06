from django import forms
from .models import Email


class EmailForm(forms.Form):
    email = forms.CharField(label='Email', initial='yourname@email.com', max_length=255)
