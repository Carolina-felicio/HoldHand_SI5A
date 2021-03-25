from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('product/<int:product_id>', views.product, name='product'),
    path('product/insert', views.insert_product, name='insert_product'),
    path('product/create', views.create_product, name='create_product'),
    path('product/delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('product/edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('my/products/', views.my_product, name='my_product'),
    path('my/answers/<int:product_id>', views.answer, name='answer')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
