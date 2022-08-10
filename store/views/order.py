from django.shortcuts import  render
from django.views import View
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class Orders(View):
    @method_decorator(auth_middleware)
    def get(self ,request):
       customer=request.session.get('customer')
       orders=Order.get_orders_by_customer(customer)
      
       return render(request,'order.html',{'order':orders})


@csrf_exempt
def handlerequest(request):
    pass

    
