"""
URL configuration for InternetShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('reg/', Registration, name = 'Registration'),
    path('auth/', Authorization, name = 'Authorization'),
    path('product/<str:slug>', product, name='product'),
    path('about/', about, name = 'About'),
    path('info/', information, name = 'Info'),
    path('cart/', cart, name='cart'),
    path('cart_remove/', cart_remove, name='cart_remove'),
    path('cart_view/', cart_view, name='cart_view'),
    path('logout/', log_out, name = 'Logout'),
    path('categories/<str:category>', categories, name='categories'),
    path('get_product_names', get_product_names, name='get_product_names'),
    path('checkout', checkout, name='checkout')
    # path('categories/<str:category>', categories_filter, name='categories_filter')
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)