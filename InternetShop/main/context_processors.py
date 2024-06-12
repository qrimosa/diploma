from .models import *

def list_products_header(request):    
    cart = request.COOKIES.get('cart')
    context = {}
    if cart:
        cart_list = cart.split(" ")
        list_products = []
        for i in cart_list:
            list_products.append(Product.objects.get(id=i))
        
        context['list_products_header'] = list_products
    return context