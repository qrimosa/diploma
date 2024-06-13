from .models import *

def list_products_header(request):    
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    productsincart = ProductInCart.objects.filter(session_key=session_key)
    context={}
    context = {
        'incartproduct': productsincart,
    }
    return context