
from django.contrib import admin
from django.urls import path
from home import views

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
   path("signup/",views.signup, name='signup'),
   path("forgot/",views.forgot, name='forgot'),
   path("cancel/",views.index, name='cancel'),
   path("cancel/",views.index, name='cancel'),
   path("form/", views.form, name='form'),



]

   


   

   

