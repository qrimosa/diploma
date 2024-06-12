from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.http import JsonResponse
from .models import *

# Create your views here.
def main(request: HttpResponse):
    return render(request, 'main/main.html')

def Registration(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if login and password and email:
            if len(password) >= 8:
                if password == repeat_password:
                    try:
                        User.objects.create_user(username = login, email = email, password = password)
                        context['email'] = ''
                        context['login'] = ''
                        context['password']  = ''
                        response = JsonResponse({'isRegister': True, 'login':login})
                    except IntegrityError:
                        return JsonResponse({'error': 'Такий користувач вже існує!'})
                    return response
                else:
                    return JsonResponse({'error': 'Паролі не співпадають!'})
            else:
                return JsonResponse({'error': 'Пароль повинен бути більше ніж 7 символів!'})
        else:
            return JsonResponse({'error': 'Ви не заповнили усі поля!'})
    return render(request, 'main/register.html', context)

def Authorization(request):
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            print(user)
            if user:
                print('login succes')
                login(request, user)
                return JsonResponse({'isLogin': True, 'username':username})
            else:
                return JsonResponse({'error': 'Логін aбо пароль невірний'})
        else:
            return JsonResponse({'error': 'Заповніть всі поля'})
    return render(request, 'main/auth.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product':product, 'characteristics': product.characteristics.get('name'), 'guide': product.guide.get('name')}
    return render(request, 'main/product.html', context)
    
    # return render(request, 'main/product.html', context)
    
def cart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('product_id')
        print(prod_id)
        context = {'products':Product.objects.get(id=prod_id)}
        response = render(request, 'main/cart.html', context)
        old_cart = request.COOKIES.get('cart')
        product_id = request.POST.get('product_id')
        if old_cart:
            product_id = old_cart + " " + product_id
        response.set_cookie('cart', product_id)
    return response

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def information(request):
    return render(request, 'main/information.html')

def cart_view(request):
    cart = request.COOKIES.get('cart')
    context = {}
    if cart:
        cart_list = cart.split(" ")
        if request.method == "POST":
            product_id = request.POST.get('product_id')
            cart_list.remove(product_id)        
        # list_products = [Product.objects.get(id = product_id) for product_id in cart_list]
        list_products = []
        for i in cart_list:
            list_products.append(Product.objects.get(id=i))
        
        context['products'] = list_products
        response = render(request, "cart/cart.html", context)
        response.set_cookie('cart', ' '.join(cart_list))
    return response