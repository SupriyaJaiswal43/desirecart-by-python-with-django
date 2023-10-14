
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('mensproduct/',views.mensproduct),
    path('womensproduct/',views.wproduct),
    path('contact/',views.contactus),
    path('kidsproduct/',views.kproduct),
    path('orders/',views.myorders),
    path('profile/',views.myprofile),
    path('viewproduct/',views.viewproduct),
    path('feedback/',views.feedback),
    path('register/',views.register),
    path('signin/',views.signin),
    path('signin1/',views.signin1),
    path('logout/',views.logout1),
    path('cart/',views.cartItems),

]