from django.shortcuts import render
from products.models import ProductProfile
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    products = ProductProfile.objects.order_by('product_name')

    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    product_per_page = paginator.get_page(page)

    data = {
        'products': product_per_page
    }
    return render(request, 'home.html', data)


def error_404(request, exception):
    data = {}
    return render(request, 'errors/error_404.html', data)
