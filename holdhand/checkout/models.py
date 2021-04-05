import uuid
from django.db import models
from django.contrib.auth.models import User

# project
from products.models import ProductProfile

# python 
from datetime import datetime

# Create your models here.


class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=100, blank=False, null=False,
    choices=(
        ('Carrinho', 'Carrinho'),
        ('Finalizado', 'Finalizado'),
        ('Pago', 'Pago'),
        ('Aguardando Pagamento', 'Aguardando Pagamento'),
    ))
    request_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Cart'

    def __str__(self):
        return str(self.id)


class ProductCart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order = models.OneToOneField(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductProfile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Products in cart'

    def __str__(self):
        return (self.product.product_name)
