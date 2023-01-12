import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from jewelries.models import Jewelry


# Create your models here.
class Order(models.Model):
    """ model for order """
    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    full_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=25, blank=False, null=False)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=80)
    county_province_state = models.CharField(max_length=90)
    country = models.CharField(max_length=90)
    post_code = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # noqa
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # noqa
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)  # noqa

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override the save method to set the order number """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        """
        Update grand total when an new item is added,
        calculate delivery costs.
        """
        self.order_total = self.orderinlineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0  # noqa
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100  # noqa
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


class OrderItem(models.Model):
    """ model for each order with items in shopping cart """
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderinlineitems')  # noqa
    jewelry = models.ForeignKey(Jewelry, null=False, blank=False, on_delete=models.CASCADE)  # noqa
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)  # noqa

    def __str__(self):
        return f'Order ID: {self.id} on order {self.order.order_number}'

    def save(self, *args, **kwargs):
        """
        Override the original save method to set orderitem total
        and update the order total
        """
        self.lineitem_total = self.jewelry.price * self.quantity
        super().save(*args, **kwargs)
