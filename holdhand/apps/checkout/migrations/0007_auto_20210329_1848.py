# Generated by Django 3.0.13 on 2021-03-29 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0023_remove_productprofile_quantity'),
        ('checkout', '0006_auto_20210329_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Cart'),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductProfile'),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
