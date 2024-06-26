from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *
import requests
# Create your views here.
def main(request: HttpResponse):
    context = {"all_products": Product.objects.all()}
    return render(request, 'main/main.html', context)

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
    products = Product.objects.all()
    context = {
        'products': products,
    }
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key
        product_id = request.POST.get('product_id')
        # product = Product.objects.get(id = product_id)
        # print(product)
        if product_id:
            try:
                product = ProductInCart.objects.get(product_id = product_id, session_key=session_key)
                product.amount += 1
                product.save()
            except:
                product = ProductInCart.objects.create(product_id=product_id,session_key=session_key, amount = 1)
            cart_count = ProductInCart.objects.filter(session_key=session_key).count()
            return JsonResponse({'cart_count': cart_count})
        # productsincart = ProductInCart.objects.filter(session_key=session_key)
    return render(request, "main/product.html", context=context)

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def information(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    context = {'products_in_cart': ProductInCart.objects.filter(session_key=session_key)}
    return render(request, 'main/information.html',context)

def cart_view(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    productsincart = ProductInCart.objects.filter(session_key=session_key)
    context = {
        'incartproduct': productsincart,
    }
    html = render_to_string('main/cart_items.html', context)
    cart_count = ProductInCart.objects.filter(session_key=session_key).count()
    return JsonResponse({"html":html, 'cart_count':cart_count})

def cart_remove(request):
    context = {}
    if request.method == 'POST':
        product_in_cart_id = request.POST.get('product_in_cart_id')
        product = ProductInCart.objects.get(id = product_in_cart_id)
        product.delete()
    return render(request, "main/base.html",context)

def log_out(request: HttpResponse):
    logout(request)
    return redirect('main')

def categories(request, category):
    category_obj = Category.objects.get(slug=category)
    products_obj = Product.objects.filter(category=category_obj)
    colors = products_obj.values('color').distinct()
    products_list = products_obj.values_list('price')
    min_price = products_list.order_by('price').first()
    max_price = products_list.order_by('price').last()
    sizes = products_obj.values('size').distinct()
    seasons = products_obj.values('season').distinct()
    context = {'category': category_obj, 'products':products_obj, 'colors':colors, 'max_price': max_price[0], 'min_price': min_price[0], 'sizes': sizes, 'seasons': seasons}
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        category_obj = Category.objects.get(slug=category)
        products = Product.objects.filter(category = category_obj,price__range=(request.GET.get('min_price'), request.GET.get('max_price')))
        colors = request.GET.getlist('colors[]')
        sizes = request.GET.getlist('sizes[]')
        seasons = request.GET.getlist('seasons[]')
        if colors:
            products = products.filter(color__in = colors)
        if sizes:
            products = products.filter(size__in = sizes)
        if seasons:
            products = products.filter(season__in = seasons)
        html = render_to_string('main/categories_filter.html', {'products': products})
        return JsonResponse({"html":html})
    return render(request, 'main/categories.html', context)

def get_product_names(request):
    return JsonResponse(list(Product.objects.all().values('name', 'slug')), safe=False)

def checkout(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key = session_key)
    sum_in_cart = 0
    for product in products_in_cart:
        sum_in_cart += product.product.price*product.amount
    context = {'products_in_cart':products_in_cart,'sum_in_cart':sum_in_cart}
    if products_in_cart.exists():
        pass
    else:
        return redirect('main')
    api_key = '8112617626b3a78db6c84bcc50a6d102'
    payload = {
        "apiKey": api_key,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityName": "Днепр",
        }
    }
    response = requests.post('https://api.novaposhta.ua/v2.0/json/', json=payload)
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            warehouses = data['data']
        addresses = [warehouse['Description'] for warehouse in warehouses if warehouse['TypeOfWarehouse']!='f9316480-5f2d-425d-bc2c-ac7cd29decf0']
        context['addresses'] = addresses
    if request.method == 'POST':
        pass
    return render(request,'main/checkout.html', context)