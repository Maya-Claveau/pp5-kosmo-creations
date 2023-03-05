"""wishlist models"""
from django.db import models
from django.contrib.auth.models import User
from jewelries.models import Jewelry
from profiles.models import UserProfile


class WishlistItem(models.Model):
    """ Wishlist model to store users favourite jewelries """
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        )
    jewelry = models.ForeignKey(
        Jewelry, on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return the string """
        return f"Wishlist ({self.user})"
