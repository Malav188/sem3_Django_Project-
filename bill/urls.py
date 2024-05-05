from django.contrib import admin

from django.urls import path
from  . import views
from django.conf import settings

urlpatterns = [
    path('', views.home,name='index'),
    path('login', views.login1,name='bill login'),
    path('signup', views.signup,name='signup'),
    path('logout', views.LogoutPage,name='logout'),
    path('entry', views.entryy,name='entryy'),
    path('pay', views.pay,name='payment'),
    path('about', views.about,name='about'),
    path('Bill', views.user_bill,name='Bill'),


]