# Generated by Django 3.2 on 2023-03-11 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_alter_newsletter_updated'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSubscriber',
            new_name='Subscription',
        ),
    ]