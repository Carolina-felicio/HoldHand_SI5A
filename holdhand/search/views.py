from django.shortcuts import render
from products.models import ProductProfile


# Create your views here.
def search(request):
    product_list = ProductProfile.objects.order_by('product_name')

    if 'search' in request.GET:
        product_to_search = request.GET['search']
        if search:
            product_list = product_list.filter(product_name__icontains=product_to_search)

    datas = {
        'products': product_list
    }
    return render(request, 'search/search.html', datas)
