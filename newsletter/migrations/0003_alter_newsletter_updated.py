# Generated by Django 3.2 on 2023-03-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_newsletter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
