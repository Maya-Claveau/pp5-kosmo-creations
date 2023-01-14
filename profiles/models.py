from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    to enable a user to have their own profile with saved delivery info
    and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=25, blank=True, null=True)
    default_address1 = models.CharField(max_length=150, blank=True, null=True)
    default_address2 = models.CharField(max_length=150, blank=True, null=True)
    default_city = models.CharField(max_length=80, blank=True, null=True)
    default_county_province_state = models.CharField(max_length=90, blank=True, null=True)  # noqa
    default_country = CountryField(blank_label='Country *')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # for existing users:  save the profile
    instance.userprofile.save()
