from django.contrib import admin

# project
from .models import Cart, ProductCart


# Register your models here.
class ListingCart(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'request_date',)
    list_display_links = ('id', 'user', )
    list_filter = ('user', 'status', )
    list_editable_changed = ('status',)
    list_per_page = 10


class ListingProductCart(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'order', 'quantity',)
    list_display_links = ('user',)
    list_filter = ('user',)
    list_per_page = 10


admin.site.register(Cart, ListingCart)
admin.site.register(ProductCart, ListingProductCart)
