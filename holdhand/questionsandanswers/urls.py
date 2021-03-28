from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('product/new/question/<int:product_id>', views.product_new_question, name='product_new_question'),
    path('product/<int:product_id>/questions', views.product_question, name='product_question'),
    path('product/<int:product_id>/questions/<int:question_id>', views.product_answer_question, name='product_answer_question'),
    path('product/<int:product_id>/usuario/respostas/<int:question_id>', views.product_resposta_usuario, name='product_resposta_usuario'),
    path('product/delete/question/<int:question_id>', views.delete_question, name='delete_question'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
