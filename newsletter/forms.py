from django import forms
from .models import Subscription, Newsletter


class NewsletterForm(forms.ModelForm):
    """ newsletter form"""
    email = forms.EmailField(label='')

    class Meta:
        """ newsletter form"""
        model = Subscription
        fields = ('email',)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        subscriber = Subscription.objects.filter(email__iexact=email)
        if subscriber.exists():
            raise forms.ValidationError("This email already subscribed!")
        return email
