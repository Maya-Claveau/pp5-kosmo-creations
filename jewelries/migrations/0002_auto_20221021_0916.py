# Generated by Django 3.2 on 2022-10-21 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewelries', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Jewelry',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
