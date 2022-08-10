from django.db import models

class customer(models.Model):
    first_name =models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=500)
    confirmpassword=models.CharField(max_length=500)
    
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_mail(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False
    
    def __str__(self):
        return self.first_name

    def isExists(self):
       
        if customer.objects.filter(email = self.email):
            return True

        return  False