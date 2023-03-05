from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """ form that use contact model """
    class Meta:
        """ meta for contact form """
        model = Contact
        fields = '__all__'
