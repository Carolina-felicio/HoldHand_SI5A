# Generated by Django 3.0.13 on 2021-03-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210329_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]