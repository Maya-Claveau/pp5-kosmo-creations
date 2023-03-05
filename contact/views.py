from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """ return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been sent! \
                    We will get back to you within 24hours.')
            return redirect('home')
        else:
            messages.error(
                request,
                'There was an error when sending the message, \
                    Please ensure the information entered is correct.'
            )
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
