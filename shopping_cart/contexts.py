from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from jewelries.models import Jewelry


def shopping_cart_contents(request):
    """ a context processor"""
    """ to make this dictionary availabe to the entire application """
    """ calculate the delivery cost according to the total in shopping_cart """

    shopping_cart_items = []
    total = 0
    product_count = 0
    shopping_cart = request.session.get('shopping_cart', {})

    for item_id, quantity in shopping_cart.items():
        jewelry = get_object_or_404(Jewelry, pk=item_id)
        total += quantity * jewelry.price
        product_count += quantity
        shopping_cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'jewelry': jewelry,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'shopping_cart_items': shopping_cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
