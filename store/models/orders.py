from django.db import models
from .customer import customer
from .product import product
import datetime
class Order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=1000,default="",blank=True)
    contact=models.CharField(max_length=15,default="",blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    
    
    @staticmethod 
    def get_orders_by_customer(customer_id):
        return Order \
            .objects \
            .filter(customer = customer_id) \
            .order_by('-date')    