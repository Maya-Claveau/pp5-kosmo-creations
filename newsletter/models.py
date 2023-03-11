from django.db import models


class NewsletterSubscriber(models.Model):
    """
    store subscriber's email
    """
    email = models.EmailField(
        max_length=254, blank=False, null=False
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICE = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    email = models.ManyToManyField(NewsletterSubscriber)
    subject = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
