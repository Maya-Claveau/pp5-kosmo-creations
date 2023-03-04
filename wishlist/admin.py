from django.contrib import admin
from . models import WishlistItem


@admin.register(WishlistItem)
class WishlistAdmin(admin.ModelAdmin):
    """wishlist admin"""
    model = WishlistItem
    fields = ('user', 'jewelry', 'created_at')
    list_display = ('pk', 'user', 'jewelry', 'created_at')
