from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(
            request, "There is nothing in your shopping cart at the moment."
            )
        return redirect(reverse('jewelries'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lk6uiI4fRay6ykcPgtj79S4i4LT4uW08jt4RGdiTdyZGKx6pJ3KFqG2DC1vDlijVdYU5UcFKEKx6XRhlg34vaky00DCvwl8vu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
