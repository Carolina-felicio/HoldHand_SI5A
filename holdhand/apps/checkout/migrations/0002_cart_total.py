# Generated by Django 3.0.13 on 2021-03-29 18:14

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8),
        ),
    ]
