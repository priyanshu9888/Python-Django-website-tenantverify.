
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from home import views
from .views import *
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name='home'),
    path('tdata/',login_required(views.tdata, login_url='user-login'), name="tdata"),

    path("tdata/",views.tdata, name='tdata'),
    path("about/",views.about, name='about'),
    path("media/",views.media, name='media'),
    path("contact/",views.contact, name='contact'),
    path("service/",views.service, name='service'),
    path('login/',views.userLogin, name="user-login"),
    path('login/otp/',views.otpLogin, name="otp-login"),
    path('registration/',views.Registration, name="Registration"),
    path('registration/otp/',views.otpRegistration, name="otp-Registration"),

    path("start/", login_required(views.start, login_url='user-login'),name="start"),
    path("apointment/",views.apointment, name='apointment'),
    path("cancel/",views.index, name='cancel'),
    path("privacy/", views.privacy,name='privacy'),
    path("termsandcondition/", views.termsandcondition,name='termsandcondition'),
    path("disclaimer/", views.disclaimer, name='disclaimer'),

    path('logout/',auth_view.LogoutView.as_view(template_name='login\logout.html'),name="logout"),
    path('email-verify/', views.email_verification, name="email-verify"),
    path('forget-password/',views.forget_password,name="forger-password"),
    path('forget-password/done/',TemplateView.as_view(template_name='forget-password-done.html')),
    path('change-password/<slug:uid>/',views.change_password,name="change-password"),

    path('users-profile/',login_required(views.userprofile, login_url='user-login'), name="users-profile"),


]