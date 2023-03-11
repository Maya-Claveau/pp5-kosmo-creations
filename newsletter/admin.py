from django.contrib import admin

from .models import NewsletterSubscriber, Newsletter

admin.site.register(NewsletterSubscriber)
admin.site.register(Newsletter)
