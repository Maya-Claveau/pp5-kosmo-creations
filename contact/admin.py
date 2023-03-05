from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin class to display email subject and message
    """
    list_display = (
        'email',
        'subject',
        'message'
    )
