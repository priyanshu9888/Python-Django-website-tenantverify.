
from django.contrib import admin
from django.urls import path
from home import views
from .views import *


urlpatterns = [
   path("", views.index, name='home'),
   path("index/", views.index, name='home'),
   path("apointment/",views.apointment, name='apointment'),
   path("home/",views.index, name='home'),
   path("about/",views.about, name='about'),
   path("cancel/",views.index, name='cancel'),
   path("service/",views.service, name='service'),
   path("media/",views.media, name='media'),
   path("contact/",views.contact, name='contact'),
   path("login/",views.login, name='login'),
   # path("signup/",views.signup, name='signup'),
   # path("forgot/",views.forgot, name='forgot'),
   path("cancel/",views.index, name='cancel'),
   path("cancel/",views.index, name='cancel'),
   path("tdata/", views.tdata, name='tdata'),
   path('register' , register , name="register"),
   path('otp' , otp , name="otp"),
   # path('login-otp', views.login_otp , name="login_otp")  


]

   


   

   

