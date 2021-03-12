from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import ProductProfile

# Create your views here.
def home(request):
    products = ProductProfile.objects.order_by('-product_name')
    
    data = {
        'products': products
    }
    
    return render(request, 'home.html', data)


def product(request, product_id):
    product = get_object_or_404(ProductProfile, pk=product_id)
    
    product_to_display = {
        'product': product
    }

    return render(request, 'products/product.html', product_to_display)


def insert_product(request):
    """
    Function get insert_product
    """
    if request.user.is_authenticated:
        return render(request, 'products/insert_product.html')
    else:
        return redirect('login')


def create_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        segment = request.POST['segment']
        store_name = request.POST['store_name']
        payment_method = request.POST['payment_method']
        description = request.POST['description']
        date_product = request.POST['date_product']
        image = request.FILES['image']
        slug = product_name
        user = get_object_or_404(User, pk=request.user.id)
        product = ProductProfile.objects.create(
            username=user, product_name=product_name, segment=segment, store_name=store_name,
            payment_method=payment_method, description=description, 
            date_product=date_product, image=image, slug=slug
        )
        product.save()
        return redirect('home')
    else:
        return render(request, 'products/insert_product.html')


def delete_product(request, product_id):       
    product = get_object_or_404(ProductProfile, pk=product_id)
    product.delete()
    
    product_to_delete ={
        'delete': product
    }
    return render(request, 'users/dashboard.html', product_to_delete)


def edit_product(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductProfile, pk=product_id)
            
        product_to_display = {
            'product': product,
        }
        return render(request, 'products/edit_product.html', product_to_display)
    else:
        return redirect('login')
