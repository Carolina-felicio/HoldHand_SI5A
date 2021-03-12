from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:product_id>', views.product, name='product'),
    path('insert_product', views.insert_product, name='insert_product'),
    path('create_product', views.create_product, name='create_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('edit_product/<int:product_id>', views.edit_product, name='edit_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
