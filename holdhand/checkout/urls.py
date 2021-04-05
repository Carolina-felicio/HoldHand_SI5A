from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# project
from . import views


urlpatterns = [
    path('my/shopping/cart', views.shopping_cart, name='shopping_cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
