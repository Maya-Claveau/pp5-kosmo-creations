from django.contrib import admin
from .models import Jewelry, Category

# Register your models here.


class JewelryAdmin(admin.ModelAdmin):
    """ class for jewelry admin """
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
        'inventory'
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """ class for category admin """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Jewelry, JewelryAdmin)
admin.site.register(Category, CategoryAdmin)
