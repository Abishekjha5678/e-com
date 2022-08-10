from django.contrib import admin
from .models.product import product
from .models.category import category
from .models.customer import customer
from .models.orders import Order
class AdminProduct(admin.ModelAdmin):
    list_display=['name', 'price','Category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminOrder(admin.ModelAdmin):
    list_display=('product','customer','price','quantity','date','address','contact')

class AdminCustomer(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email')

admin.site.register(product,AdminProduct)
admin.site.register(category,AdminCategory)
admin.site.register(customer,AdminCustomer)
admin.site.register(Order,AdminOrder)
# Register your models here.
