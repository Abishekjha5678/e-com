
from django import views
from django.urls.conf import path
from django.views.generic.base import View
from .views.home import Index
from .views.login import Login,logout
from .views.signup import Signup
from django.urls import path
from .views.cart import Cart
from .views.contact import Contact
from .views.order import Orders
from .views.order import handlerequest
from .views.checkout import Checkout
from .views.notification import Notification
urlpatterns = [
    path('', Index.as_view(),name='homepage'),
    path('signup',Signup.as_view(),name ='signup'),
    path('login',Login.as_view(),name='login'),#django decide which method has to run through as_view mehtod 
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('contact',Contact.as_view(),name='contact'),
    path('check-out',Checkout.as_view(),name='check-out'),
    path('order',Orders.as_view(),name='order'),
    path('handlerequest',handlerequest,name='handlereuest'),
    path('notification',Notification.as_view(),name='notification')
]
