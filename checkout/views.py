from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse  # noqa
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderItem

from jewelries.models import Jewelry
from shopping_cart.contexts import shopping_cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'shopping_cart': json.dumps(request.session.get('shopping_cart', {})),  # noqa
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ to handle the checkout process using stripe """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_cart = request.session.get('shopping_cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'city': request.POST['city'],
            'county_province_state': request.POST['county_province_state'],
            'post_code': request.POST['post_code'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_shopping_cart = json.dumps(shopping_cart)
            order.save()
            for item_id, item_data in shopping_cart.items():
                try:
                    jewelry = Jewelry.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        jewelry=jewelry,
                        quantity=item_data,
                    )
                    order_item.save()
                except jewelry.DoesNotExist:
                    messages.error(request, (
                        "One of the Jewelry in your shopping cart wasn't found."  # noqa
                        " Please let us know and we will assist you!"
                    ))
                    order.delete()
                    return redirect(reverse('view_shopping_cart'))
                request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))  # noqa
        else:
            messages.error(request, 'Error detected in your form. \
                Please make sure the information entered are correct.')
    else:
        shopping_cart = request.session.get('shopping_cart', {})
        if not shopping_cart:
            messages.error(
                request, "There is nothing in your shopping cart at the moment."  # noqa
                )
            return redirect(reverse('jewelries'))

        current_shopping_cart = shopping_cart_contents(request)
        total = current_shopping_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successful! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}. \
        Thank you for shopping with us.')

    if 'shopping_cart' in request.session:
        del request.session['shopping_cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
