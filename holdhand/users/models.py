from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    segment = models.TextField(max_length=300, null=True, blank=True)
    store_name = models.TextField(max_length=300, null=True, blank=True)
    address = models.TextField(max_length=150, null=True, blank=True)
    payment_method = models.TextField(max_length=255, null=True, blank=True)
