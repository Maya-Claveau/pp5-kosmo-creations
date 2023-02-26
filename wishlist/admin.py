from django.contrib import admin
from . models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """wishlist admin"""
    model = Wishlist
    fields = ('user', 'jewelry', 'created_at')
    list_display = ('pk', 'user', 'jewelry', 'created_at')
