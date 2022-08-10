from django import views
from django.http.response import HttpResponse
from django.shortcuts import render
from store.models.product import product
from django.views import View
from store.models.product import product
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Cart(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        Cart_list=list(request.session.get('cart').keys())
        products=product.get_product_by_ID(Cart_list)
        return render(request,'cart.html',{'products':products})


    
