# Generated by Django 3.0.13 on 2021-03-30 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_remove_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcart',
            name='total_price',
        ),
    ]
