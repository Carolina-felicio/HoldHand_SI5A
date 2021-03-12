from django.contrib import admin
from .models import ProductProfile


# Register your models here.
class ProductProfileList(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('product_name', )}
    list_display = (
        'username', 'product_name', 'segment', 'store_name', 'payment_method',
        'date_product', 'image',
    )
    list_display_links = ('username',)
    list_filter = ('segment',)
    list_per_page = 10


admin.site.register(ProductProfile, ProductProfileList)
