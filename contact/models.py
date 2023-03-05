from django.db import models


class Contact(models.Model):
    """ model for contact app """
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email
