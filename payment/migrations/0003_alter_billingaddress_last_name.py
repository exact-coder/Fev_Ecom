# Generated by Django 4.1.3 on 2023-01-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_billingaddress_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name'),
        ),
    ]