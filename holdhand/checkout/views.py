from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, ProductCart
from products.models import ProductProfile
from users.models import UserProfile

# python
from decimal import Decimal


# Create your views here.
def shopping_cart(request):
    if request.user.is_authenticated:

        try:
            cart = Cart.objects.get(user=request.user, status="Carrinho")
        except Cart.DoesNotExist:
            cart = Cart(user=request.user, status="Carrinho")

        if request.method == 'POST':
            product_id = request.POST['product']
            product = ProductProfile.objects.get(id=product_id)
            quantity = request.POST['quantity']
            user = request.user

            if quantity == '' or quantity == '0' or quantity < str(0):
                quantity = 1

            try:
                item = ProductCart.objects.get(order=cart, product=product)
            except ProductCart.DoesNotExist:
                item = ProductCart(order=cart, product=product, quantity=0, user=user)

            item.quantity = int(quantity)
            item.user = user
            cart.save()
            item.save()

        data = {
            'cart': cart,
            'itens': ProductCart.objects.filter(order=cart)
        }

        return render(request, 'cart/shopping_cart.html', data)
    return redirect('login')
