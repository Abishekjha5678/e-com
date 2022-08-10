from django import views
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View




class Notification(View):
    def get(self, request):
       return render(request,'notification.html')
    

    
