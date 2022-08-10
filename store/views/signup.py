from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from store.models.customer import customer
from django.contrib.auth.hashers import make_password
from django.views import View


   
class Signup(View):
    def get(self, request):
        return render(request,'signup.html')
    
    def post(self,request):
        PostData= request.POST
        Firstname=PostData.get('Firstname')
        Lastname=PostData.get('Lastname')
        number=PostData.get('number')
        email=PostData.get('email')
        password=PostData.get('password')  
        confirm_password=PostData.get('confirmpassword')
        
        value= {
        'first_name':Firstname,
        'last_name' :Lastname,
        'number': number,
        'email': email
        }
        error_message =None
        Customer=customer(first_name=Firstname, last_name=Lastname,phone=number,email=email,password=password,confirmpassword=confirm_password)
        error_message=self.validateCustomer(Customer)    
        #saving
    
        if not error_message:
            Customer.password=make_password(Customer.password)
            Customer.confirmpassword=make_password(Customer.confirmpassword)
           
            if password==confirm_password:
                 Customer.register()
                 return redirect('homepage')
            else:
                data={
                'error_message':"Password Not Matched",
                'values':value
                }
                return render(request,'signup.html',data) 
        else:
            data={
                'error_message': error_message,
                'values' :value
            }
        return render(request,'signup.html',data)


        #Validting User

    def validateCustomer(self,Customer):
        error_message=None;
        if (not Customer.first_name):
            error_message='First name Required'
        elif len(Customer.first_name) <4:
            error_message="First Name must be 4 char long"
        elif (not Customer.last_name):
            error_message='Last name Required'
        elif len(Customer.last_name) <3:
            error_message="Last Name must be 4 char long"
        elif (not Customer.phone):
            error_message='Number Required'
        elif len(Customer.phone) <10:
            error_message="Phone Number must be 10 digit long"
        elif (not Customer.email):
            error_message='Email Required'
        elif len(Customer.email) <6:
            error_message="Email Id must be 6 character long"
        elif (not Customer.password):
            error_message='Password Required'
        elif len(Customer.password) <6:
            error_message="Password must be 6 digit long"
        elif Customer.isExists():
            error_message='This Email Id is already Registered'
        return error_message

