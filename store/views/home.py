from django import http
from django import views
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.product import product
from store.models.category import category
from store.models.customer import customer
from django.contrib.auth.hashers import make_password, check_password 
from django.views import View

# Create your views here.

class Index(View):
   
    def get(self,request):
       
        products = None
        #return render(request, 'orders/order.html')
        Category=category.get_all_categories()
        CategoryID =request.GET.get('category')
        if CategoryID:
            products=product.get_all_product_by_Categoryid(CategoryID);
            
        else:
            products=product.get_all_products();
        data={}
        data['products']=products   
        data['Category']=Category 
        
        return render(request, 'index.html', data)
        # return HttpResponse("test")

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart = request.session.get('cart')
        
        if cart:
            quantity=cart.get(product)
           
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                    
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        #print(request.session['cart'])
        request.session['cart']=cart
        
        return redirect('homepage')

       
    



        