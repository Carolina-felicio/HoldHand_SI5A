from django.contrib.auth.models import User
from django.db import models
from products.models import ProductProfile


# Create your models here.


class ProductQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductProfile, on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        verbose_name_plural = "Product Questions"

    @property
    def get_answers(self):
        return self.productanswer_set.filter()

    def __str__(self):
        return self.question


class ProductAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_question = models.ForeignKey(ProductQuestion, on_delete=models.CASCADE)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.answer
