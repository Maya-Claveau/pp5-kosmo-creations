"""wishlist models"""
from django.db import models
from django.contrib.auth.models import User
from jewelries.models import Jewelry
from profiles.models import UserProfile


class WishlistItem(models.Model):
    """ Wishlist model to store users favourite jewelries """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='wishlist', null=False, blank=False)
    jewelry = models.ForeignKey(
        Jewelry, on_delete=models.CASCADE, related_name='wishlist',
        null=False, blank=False)

    def __str__(self):
        """ return the string """
        return f"{self.quantity} of {self.jewelry}"

    # def get_jewelries(self):
    #     """ return all the jewelries in the wishlist """
    #     return self.jewelries.all()
