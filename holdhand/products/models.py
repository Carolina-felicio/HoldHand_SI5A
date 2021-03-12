from django.db import models
from django.contrib.auth.models import User

# python 
from datetime import datetime


# Create your models here.
class ProductProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=False)
    segment = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date_product = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='images/%d/%m/%Y/', blank=True)

    class Meta:
        verbose_name_plural = 'Products Profile'

    def __str__(self):
        return ("Nome do produto - {product}").format(product=self.product_name)
