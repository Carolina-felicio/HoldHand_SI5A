# Generated by Django 3.0.13 on 2021-03-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210321_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprofile',
            name='payment_method',
            field=models.CharField(max_length=100),
        ),
    ]