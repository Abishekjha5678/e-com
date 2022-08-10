from django.shortcuts import redirect, render
from django.views import View
from store.models.customer import customer
from store.models.product import product
from store.models.orders import Order
class Checkout(View):
    def post(self, request):
        address=request.POST.get('Address')
        contact=request.POST.get('Contact')
        Customer=request.session.get('customer')  
        cart=request.session.get('cart')
        #object
        
        for key in list(cart.keys()):
            products=product.get_all_product_by_Categoryid(key)  
            order=Order(customer=customer(id=Customer),product=products,price=products.price,address=address,contact=contact,quantity=cart.get(key))
            order.save()
        request.session['cart']={}
        
        return redirect('cart')   

