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

def product(request, product):
    
    context = {'product':Product.objects.get(name=product)}
    return render(request, 'main/product.html', context)

def product2(request: HttpResponse):
    
    return render(request, 'main/product2.html')
    # products = Product.objects.all()
    # context = {"products": products}
    
    # if request.method == 'POST':
    #     pass
        

def about(request):
    context = {}
    return render(request, 'main/about.html', context)