# Generated by Django 3.1.7 on 2021-03-22 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_productprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprofile',
            name='payment_method',
            field=models.CharField(choices=[('PIX', 'PIX'), ('Ticket', 'Ticket'), ('Credit card | debit', 'Credit card | debit'), ('Exchange involving product', 'Exchange involving product')], max_length=100),
        ),
    ]
