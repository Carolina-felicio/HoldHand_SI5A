from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm, UserDeleteForm, PythonProResetForm
from checkout.models import Cart
from django.contrib.auth.views import PasswordResetForm, PasswordResetView

import json
import urllib

# Create your views here.
def register(request):
    """
    Function at register user
    """
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username is None:
            return redirect('register')
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        email2 = request.POST['email2']
        password = request.POST['password']
        password2 = request.POST['password2']
        address = request.POST['address']
        zip_code = request.POST['zip_code']
        city = request.POST['city']
        uf = request.POST['uf']
        number = request.POST['number']
        district = request.POST['district']
        complement = request.POST['complement']
        phone = request.POST['phone']
        cell_phone = request.POST['cell_phone']

        if (campo_vazio(username) or username is None):
            messages.erro(
                request, 'WARNING!!! The user field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(name) or name is None):
            messages.error(
                request, 'WARNING!!! The name field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(surname) or surname is None):
            messages.error(
                request, 'WARNING !!! The surname field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(email) or email is None):
            messages.error(
                request, 'WARNING!!! The email field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(email2) or email2 is None):
            messages.error(
                request, 'WARNING!!! The confirmation email field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(password) or password is None):
            messages.error(
                request, 'WARNING!!! The password field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(password2) or password2 is None):
            messages.error(
                request, 'WARNING!!! The confirmation password field cannot be empty'
            )
            return redirect('register')
        # Address
        if (campo_vazio(address) or address is None):
            messages.error(
                request, 'WARNING!!! The address field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(zip_code) or zip_code is None):
            messages.error(
                request, 'WARNING!!! The zip_code field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(city) or city is None):
            messages.error(
                request, 'WARNING!!! The city field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(uf) or uf is None):
            messages.error(
                request, 'WARNING!!! The zip_code field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(district) or district is None):
            messages.error(
                request, 'WARNING!!! The district field cannot be empty'
            )
            return redirect('register')

        if (campo_vazio(number) or number is None):
            messages.error(
                request, 'WARNING!!! The number field cannot be empty'
            )
            return redirect('register')
        # Address

        if (senhas_nao_sao_iguais(password, password2)):
            messages.error(
                request, 'WARNING!!! The password and password confirmation fields do not match'
            )
            return redirect('register')

        if (email_nao_sao_iguais(email, email2)):
            messages.error(
                request, 'WARNING!!! The e-mail and e-mail confirmation fields do not match'
            )
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(
                request, 'WARNING!!! This email is already registered'
            )
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(
                request, 'WARNING!!! This username already exists. Please insert another'
            )
            return redirect('register')
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=name, last_name=surname
        )
        user_address = UserProfile.objects.create(
            username=user, address=address, number=number, district=district,
            city=city, uf=uf, complement=complement, zip_code=zip_code,
            cell_phone=cell_phone, phone=phone
        )
        cart = Cart.objects.create(user=user, status="Carrinho")

        user.save()
        user_address.save()
        cart.save()
        datas = {
            'user': user,
            'user_address': user_address,
            'cart': cart
        }
        messages.info(
            request, 'usuário criado com sucesso'
        )
        return render(request, 'two_factor/core/login.html', datas)
    else:
        return render(request, 'users/register.html')


def login(request):
    """
    function login
    """
    dados_cookie = {
        'email': request.COOKIES.get('email'),
        'password': request.COOKIES.get('password')
    }

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']

        if (campo_vazio(email) or campo_vazio(senha)):
            messages.error(
                request, 'WARNING!!! E-mail and / or password fields cannot be empty'
            )
            return redirect('login')
        
        if (campo_vazio(email) and campo_vazio(senha)):
            messages.error(
                request, 'WARNING!!! E-mail and password fields cannot be empty'
            )
            return redirect('login')

        if User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list(
                'username', flat=True
            ).get()
            user = auth.authenticate(request, username=name, password=senha)

            if user is not None:
                auth.login(request, user)
                response = redirect('home')
                response.set_cookie(key='email', value=email)
                return response

        if User.objects.filter(email=email).exists():
            messages.error(
                request, 'WARNING!!! Invalid email and / or password'
            )
        else:
            messages.error(
                request, 'WARNING!!! This email is not registered'
            )

        response = render(request, 'users/login.html')
        response.set_cookie(key='email', value=email)
        return response
    return render(request, 'two_factor/core/login.html', dados_cookie)


def my_data(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        user_form = UserForm(instance=user)

        try:
            user_profile = UserProfile.objects.get(username=user)
        except:
            user_profile = UserProfile()
            user_profile.username = user
            user_profile.save()

        profile_form = UserProfileForm(instance=user_profile)

        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user.first_name = user_form.cleaned_data['first_name']
                user.last_name = user_form.cleaned_data['last_name']
                user.email = user_form.cleaned_data['email']

                user_profile.phone = profile_form.cleaned_data['phone']
                user_profile.cell_phone = profile_form.cleaned_data['cell_phone']
                user_profile.zip_code = profile_form.cleaned_data['zip_code']
                user_profile.address = profile_form.cleaned_data['address']
                user_profile.district = profile_form.cleaned_data['district']
                user_profile.number = profile_form.cleaned_data['number']
                user_profile.complement = profile_form.cleaned_data['complement']
                user_profile.city = profile_form.cleaned_data['city']
                user_profile.uf = profile_form.cleaned_data['uf']
                
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
                    user.save()
                    user_profile.save()
                    messages.success(request, 'Data has been successfully changed!')
                else:
                    messages.error(request, 'Invalid recaptcha and/or recaptcha not selected. Please try again.')
                
                return redirect('my_data')

        data = {
            'user_form': user_form,
            'profile_form': profile_form,
            'user': user
        }
        return render(request, 'users/my_data.html', data)
    return redirect('two_factor:login')


def delete_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            delete_form = UserDeleteForm(request.POST, instance=request.user)
            user = request.user
            user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('delete_user')
        else:
            delete_form = UserDeleteForm(instance=request.user)

        context = {
            'delete_form': delete_form
        }

        return render(request, 'users/delete_user.html', context)
    return redirect('two_factor:login')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html')
    return redirect('two_factor:login')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    return redirect('two_factor:login')


def logout(request):
    """
    Function logout
    """
    auth.logout(request)
    return redirect('two_factor:login')


def campo_vazio(campo):
    """
    Função que verifica se um determinado campo, de cadastro ou login está vazio
    """
    return not campo.strip()


def senhas_nao_sao_iguais(password, password2):
    """
    Função que verifica se as senha são diferentes para realizar o cadastro
    """
    return password != password2


def email_nao_sao_iguais(email, email2):
    """
    Função que verifica se os emails não são iguais para realizar o cadastro
    """
    return email != email2
