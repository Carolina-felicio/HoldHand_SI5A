# Generated by Django 3.0.13 on 2021-03-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210323_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productprofile',
            old_name='image',
            new_name='image_one',
        ),
        migrations.AddField(
            model_name='productprofile',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='images/%d/%m/%Y/'),
        ),
        migrations.AddField(
            model_name='productprofile',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='images/%d/%m/%Y/'),
        ),
    ]
