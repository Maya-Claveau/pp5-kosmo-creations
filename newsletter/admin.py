from django.contrib import admin
from .models import Subscription, Newsletter


class SubscriptionAdmin(admin.ModelAdmin):
    """ display Subscription model in Admin """
    list_display = (
        'email', 'date_added'
    )

    search_fields = ('email', 'date_added')
    ordering = ('date_added',)


class NewsletterAdmin(admin.ModelAdmin):
    """ display newsletter model in Admin """
    list_display = (
        'subject', 'status', 'created', 'updated'
    )

    search_fields = ('title', 'message')


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
