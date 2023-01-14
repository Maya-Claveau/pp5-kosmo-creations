from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderItem
from jewelries.models import Jewelry

import json
import time
import stripe


class StripeWH_Handler:
    """ handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ send a confirmation email to the user """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """ handle a general/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ handle the payment_intent.succeeded webhook event """
        intent = event.data.object
        pid = intent.id
        shopping_cart = intent.metadata.shopping_cart

        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county_province_state__iexact=shipping_details.address.state,  # noqa
                    grand_total=grand_total,
                    original_shopping_cart=shopping_cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',  # noqa
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    post_code=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county_province_state=shipping_details.address.state,
                    original_shopping_cart=shopping_cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(shopping_cart).items():
                    jewelry = Jewelry.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        jewelry=jewelry,
                        quantity=item_data,
                    )
                    order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook', status=200  # noqa
        )

    def handle_payment_intent_payment_failed(self, event):
        """ handle the payment_intent.payment_failed webhook event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )
