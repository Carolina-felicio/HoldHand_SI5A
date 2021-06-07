from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseNotFound, Http404
from django.core.paginator import Paginator
import json
import urllib
from django.contrib import auth, messages
from django.conf import settings

# project
from .models import ProductProfile
from .forms import ProductForm
from questionsandanswers.models import ProductQuestion
from questionsandanswers.forms import ProductQuestionForm
from users.models import UserProfile
from checkout.models import Cart

# Create your views here.


def product(request, product_id):
    try:
        product = ProductProfile.objects.get(pk=product_id)
        questions = ProductQuestion.objects.filter(product=product).order_by('user')
        form = ProductQuestionForm()

        paginator = Paginator(questions, 4)
        page = request.GET.get('page')
        product_per_page = paginator.get_page(page)
        
        product_to_display = {
            'form': form,
            'product': product,
            'questions': product_per_page
        }
    except ProductProfile.DoesNotExist:
        response = render(request, 'errors/error_404.html')
        return HttpResponseNotFound(response.content)
    return render(request, 'products/product.html', product_to_display)


def my_product(request):
    if request.user.is_authenticated:
        identification = request.user.id
        products = ProductProfile.objects.order_by('-date_product').filter(username=identification)

        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        product_per_page = paginator.get_page(page)

        datas = {
            'products': product_per_page
        }
        return render(request, 'products/my_products.html', datas)
    else:
        return redirect('login')


def insert_product(request):
    """
    Function get insert_product
    """
    if request.user.is_authenticated:
        return render(request, 'products/insert_product.html')
    return redirect('two_factor:login')


def create_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            product_name = request.POST['product_name']
            segment = request.POST['segment']
            store_name = request.POST['store_name']
            payment_method = request.POST['payment_method']
            description = request.POST['description']
            date_product = request.POST['date_product']
            image_one = request.FILES['image_one']
            image_two = request.FILES['image_two']
            image_three = request.FILES['image_three']
            price = request.POST['price']
            slug = request.POST['product_name']
            user = get_object_or_404(User, pk=request.user.id)
            profile = get_object_or_404(UserProfile, pk=request.user.id)
            product = ProductProfile.objects.create(
                username=user, product_name=product_name, segment=segment, store_name=store_name,
                payment_method=payment_method, description=description, date_product=date_product,
                image_one=image_one, image_two=image_two, image_three=image_three, profile=profile,
                slug=slug, price=price
            )
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/insert_product.html')
    return redirect('two_factor:login')


def delete_product(request, product_id):
    product = get_object_or_404(ProductProfile, pk=product_id)
    product.delete()

    product_to_delete = {
        'delete': product
    }
    return render(request, 'users/dashboard.html', product_to_delete)


def edit_product(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductProfile, pk=product_id)
        form = ProductForm(instance=product)
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product.product_name = form.cleaned_data['product_name']
                product.segment = form.cleaned_data['segment']
                product.store_name = form.cleaned_data['store_name']
                product.payment_method = form.cleaned_data['payment_method']
                product.description = form.cleaned_data['description']
                
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                
                if result['success']:
                    product.save()
                    messages.success(request, 'Data has been successfully changed!')
                else:
                    messages.error(request, 'Invalid recaptcha and/or recaptcha not selected. Please try again.')
                
                return redirect('profile')
            
        
        product_to_display = {
            'product': product,
            'form': form
        }
        return render(request, 'products/edit_product.html', product_to_display)
    return redirect('two_factor:login')


def answer(request, product_id):
    product = get_object_or_404(ProductProfile, pk=product_id)

    data = {
        'product': product
    }
    return render(request, 'products/answer.html', data)
