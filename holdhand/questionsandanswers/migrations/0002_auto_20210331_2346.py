# Generated by Django 3.0.13 on 2021-04-01 02:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questionsandanswers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productanswer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='productquestion',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]