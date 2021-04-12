from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my_panel_and_profile/', views.dashboard, name='dashboard'),
    path('my/datas/', views.my_data, name='my_data'),
    path('delete/my/user/', views.delete_user, name='delete_user'),
    path('my/profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
