from django import forms
from .models import Subscription, Newsletter


class NewsletterForm(forms.ModelForm):
    """ newsletter form"""
    class Meta:
        """ newsletter form"""
        model = Subscription
        fields = ['email']
