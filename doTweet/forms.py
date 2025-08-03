from django import forms
from .models import Tweet

class TweerForm(forms.ModelForm):
    class Meta:
        model: Tweet
        feilds = ['text', 'photo']
        