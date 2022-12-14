from django.db import models


class Category(models.Model):
    """ model for category """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Jewelry(models.Model):
    """ model for jewelries """

    class Meta:
        verbose_name_plural = 'Jewelries'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    image = models.ImageField(null=True, blank=True)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def has_inventory(self):
        return self.inventory > 0
