from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.template.loader import render_to_string
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
        # productsincart = ProductInCart.objects.filter(session_key=session_key)
    return render(request, "main/product.html", context=context)

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def information(request):
    return render(request, 'main/information.html')

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
    return JsonResponse({"html":html})

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
    context = {'category': category_obj, 'products':products_obj, 'colors':colors, 'max_price': max_price[0], 'min_price': min_price[0]}
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        category_obj = Category.objects.get(slug=category)
        products = Product.objects.filter(category = category_obj,price__range=(request.GET.get('min_price'), request.GET.get('max_price')))
        colors = request.GET.getlist('colors[]')
        if colors:
            products = products.filter(color__in = colors)
        html = render_to_string('main/categories_filter.html', {'products': products})
        return JsonResponse({"html":html})
    return render(request, 'main/categories.html', context)