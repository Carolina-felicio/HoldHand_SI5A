import uuid
from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile

# python
from datetime import datetime
from decimal import Decimal


# Create your models here.
class ProductProfile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    segment = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    PAYMENTS_CHOICES = (('PIX', 'PIX'), ('Ticket', 'Ticket'), ('Credit card | debit', 'Credit card | debit'), ('Exchange involving product', 'Exchange involving product'),)
    payment_method = models.CharField(max_length=100, choices=PAYMENTS_CHOICES)
    description = models.TextField(max_length=500)
    date_product = models.DateTimeField(default=datetime.now, blank=True)
    image_one = models.ImageField(upload_to='images/', blank=True)
    image_two = models.ImageField(upload_to='images/', blank=True)
    image_three = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))

    @property
    def questions_no_answer(self):
        return self.productquestion_set.filter(productanswer__isnull=True)

    class Meta:
        verbose_name_plural = 'Products Profile'

    def __str__(self):
        return ("Nome do produto - {product}").format(product=self.product_name)
