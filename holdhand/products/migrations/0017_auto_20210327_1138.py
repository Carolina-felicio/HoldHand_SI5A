# Generated by Django 3.0.13 on 2021-03-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210325_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprofile',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productprofile',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productprofile',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
