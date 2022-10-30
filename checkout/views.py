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
    }

    return render(request, template, context)
