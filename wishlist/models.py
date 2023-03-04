"""wishlist models"""
from django.db import models
from jewelries.models import Jewelry
from profiles.models import UserProfile


class WishlistItem(models.Model):
    """ Wishlist model to store users favourite jewelries """
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        related_name='wishlist', null=False, blank=False)
    jewelry = models.ForeignKey(
        Jewelry, on_delete=models.CASCADE, related_name='wishlist',
        null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        """ return the string """
        return self.jewelry.name

    def get_jewelries(self):
        """ return all the jewelries in the wishlist """
        return self.jewelries.all()
