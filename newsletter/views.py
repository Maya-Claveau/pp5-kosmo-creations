from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Subscription
from .forms import NewsletterForm


def newsletter_view(request):
    """ return the newsletter page """
    return render(request, 'newsletter/newsletter.html')
