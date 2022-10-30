from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    """ for the OrderItem model."""
    model = OrderItem

    list_display = (
        'order',
        'quantity',
    )

    list_filter = (
        'order',
    )

    search_fields = (
        'order',
        'quantity',
    )

    ordering = ('order',)


class OrderAdmin(admin.ModelAdmin):
    """  for the Order model """

    inlines = (OrderItemAdmin,)

    readonly_fields = (
        'order_number', 'created_on',
        'delivery_cost', 'order_total',
        'grand_total',
        )

    fields = (
        'order_number', 'created_on', 'full_name',
        'email', 'phone', 'address1',
        'address2', 'city', 'county_province_state',
        'post_code', 'country', 'order_total', 'grand_total',
        'delivery_cost',
        )

    list_display = (
        'order_number', 'created_on', 'full_name',
        'order_total', 'grand_total',
        'delivery_cost',
        )

    ordering = ('-date',)
    ordering = ('-created_on',)


admin.site.register(Order, OrderAdmin)
