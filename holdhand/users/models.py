import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    username = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    district = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    complement = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    uf = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return ("{name} {surname}").format(name=self.username.first_name, surname=self.username.last_name)
