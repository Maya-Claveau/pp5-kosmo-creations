from django.contrib import admin
from .models import NewsletterSubscriber, Newsletter


class SubscriberAdmin(admin.ModelAdmin):
    """ display NewsletterSubscriber model in Admin """
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


admin.site.register(NewsletterSubscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
