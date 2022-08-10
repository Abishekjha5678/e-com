from django import views
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View




class Contact(View):
    def get(self, request):
       return render(request,'contact.html')
    def post(self,request):
        return render(request,'contact.html')
    

    
