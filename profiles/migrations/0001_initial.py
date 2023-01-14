# Generated by Django 3.2 on 2023-01-14 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('default_address1', models.CharField(blank=True, max_length=150, null=True)),
                ('default_address2', models.CharField(blank=True, max_length=150, null=True)),
                ('default_city', models.CharField(blank=True, max_length=80, null=True)),
                ('default_county_province_state', models.CharField(blank=True, max_length=90, null=True)),
                ('default_country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]