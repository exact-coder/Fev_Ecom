# Generated by Django 4.1.3 on 2023-01-18 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Coupon Code')),
                ('valid_from', models.DateTimeField(verbose_name='Coupon Start Time')),
                ('valid_to', models.DateTimeField(verbose_name='Coupon End Time')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(80)], verbose_name='Persentage of Discount')),
                ('active', models.BooleanField(verbose_name='Coupon Code Active or Not')),
            ],
            options={
                'verbose_name': 'Coupon Code',
            },
        ),
    ]
