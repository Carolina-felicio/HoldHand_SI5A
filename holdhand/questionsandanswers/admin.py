from django.contrib import admin
from .models import ProductAnswer, ProductQuestion
# Register your models here.


class ProductAnswerInline(admin.StackedInline):
    model = ProductAnswer
    can_delete = False
    

class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'question', 'user')
    inlines = (ProductAnswerInline,)


admin.site.register(ProductQuestion, ProductQuestionAdmin)