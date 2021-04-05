# Generated by Django 3.0.13 on 2021-03-29 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_remove_productprofile_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0008_auto_20210329_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='checkout.Cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcart',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.ProductProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
