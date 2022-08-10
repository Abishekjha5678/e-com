from django.db import models 
from .category import category 

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    Category = models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    description =models.CharField(max_length=200,default="",null=True,blank=True)
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_all_product_by_Categoryid(category_id):
        if category_id:
            return product.objects.get(id = category_id)
        else:
           return product.get_all_products()

    @staticmethod
    def get_product_by_ID(ids):
        return product.objects.filter(id__in=ids) #to get the list of id       
        
