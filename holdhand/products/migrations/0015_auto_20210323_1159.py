# Generated by Django 3.0.13 on 2021-03-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210322_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprofile',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]