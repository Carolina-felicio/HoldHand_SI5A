from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import ProductQuestion, ProductAnswer
from .forms import ProductQuestionForm, AnswerQuestionForm
from products.models import ProductProfile


# Create your views here.


def product_new_question(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductProfile, id=product_id)
        
        if request.method == 'POST':
            form = ProductQuestionForm(request.POST)
            if form.is_valid():
                question = ProductQuestion()
                question.user = request.user
                question.product = product
                question.question = form.cleaned_data['question']
                question.save()
            
        return redirect('product', product.id)
    return redirect('login')

def product_question(request, product_id):
    product = get_object_or_404(ProductProfile, pk=product_id)
    
    data = {
        'product': product
    }
    
    return render(request, 'products/product_question.html', data)


def product_answer_question(request, product_id, question_id):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductProfile, pk=product_id)
        question = get_object_or_404(ProductQuestion, pk=question_id)
        
        form = AnswerQuestionForm()
        
        if request.method == 'POST':
            form = AnswerQuestionForm(request.POST)
            if form.is_valid():
                product_answer = ProductAnswer()
                product_answer.user = request.user
                product_answer.answer = form.cleaned_data['answer']
                product_answer.product_question = question
                product_answer.save()
                
                return redirect('product_question', product.id)
        
        data = {
            'form': form,
            'product': product,
            'question': question
        }
        
        return render(request, 'products/product_answer_question.html', data)
    return redirect('login')


def delete_question(request, question_id):
    question = get_object_or_404(ProductQuestion, pk=question_id)
    question.delete()

    question_to_delete = {
        'delete': question
    }
    return render(request, 'products/my_products.html', question_to_delete)


def product_resposta_usuario(request, product_id, question_id):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductProfile, pk=product_id)
        question = get_object_or_404(ProductQuestion, pk=question_id)
        
        form = AnswerQuestionForm()
        
        if request.method == 'POST':
            form = AnswerQuestionForm(request.POST)
            if form.is_valid():
                product_answer = ProductAnswer()
                product_answer.user = request.user
                product_answer.answer = form.cleaned_data['answer']
                product_answer.product_question = question
                product_answer.save()
                
                return redirect('product_question', product.id)
        
        data = {
            'form': form,
            'product': product,
            'question': question
        }
        
        return render(request, 'products/product_answer_question.html', data)
    return redirect('login')