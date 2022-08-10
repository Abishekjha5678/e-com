from django.shortcuts import render,redirect
from store.models.customer import customer
from django.contrib.auth.hashers import check_password 
from django.views import View



class Login(View):
    def get(self, request):
        return render(request,'login.html')
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        Customer=customer.get_customer_by_mail(email)
        error_message=None
        if Customer:
           flag= check_password(password,Customer.password)
           if flag:
               request.session['customer']=Customer.id
               return redirect('homepage')        
           else:
                error_message="Invalid password"   
        else:
            error_message="Invalid Email or Password"
        return render(request,'login.html', {'error':error_message})        

def logout(request):
   request.session.clear()
   return redirect('login')
