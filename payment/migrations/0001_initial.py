# Generated by Django 4.1.3 on 2023-01-18 17:34

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
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address1', models.TextField(blank=True, null=True, verbose_name='Address1')),
                ('address2', models.TextField(blank=True, null=True, verbose_name='Address2')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('zipcode', models.CharField(blank=True, max_length=50, null=True, verbose_name='Zip Code')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Phone Number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
