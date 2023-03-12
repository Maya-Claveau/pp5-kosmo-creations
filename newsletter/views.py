from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Subscription
from .forms import NewsletterForm


def newsletter_view(request):
    """ return the newsletter page """
    all_subscribers = Subscription.objects.all()
    form = NewsletterForm()
    context = {
        'form': form,
        'all_subscribers': all_subscribers,
    }
    return render(request, 'newsletter/newsletter.html', context)
