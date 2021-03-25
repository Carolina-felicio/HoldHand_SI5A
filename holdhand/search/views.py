from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import ProductProfile


# Create your views here.
def search(request):
    product_list = ProductProfile.objects.order_by('product_name')

    if 'search' in request.GET:
        product_to_search = request.GET['search']
        if search:
            product_list = product_list.filter(product_name__icontains=product_to_search)

    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    product_per_page = paginator.get_page(page)
    
    datas = {
        'products': product_per_page
    }
    return render(request, 'search/search.html', datas)
