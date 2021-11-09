from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from home.admin import ApointmentAdmin

from .models import Apointment
from .models import Contact


from django.contrib import messages


#         # Create your views here.


def index(request):

   return render(request, 'index.html')


def apointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        option=request.POST.get('option')
        apointment=Apointment(name=name,email=email, phone=phone,desc=desc,option=option)
        apointment.save()
        messages.success(request, 'Apointmnet form submited successfully')        
        return redirect("apointment")
    return render(request,"apointment.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email, phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Contact form submited successfully')        
       
        return redirect("contact")
    return render(request,"contact.html")
   

def home(request):

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def cancel(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')




def media(request):
    return render(request, 'media.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def forgot(request):
    return render(request, 'forgot.html')
def form(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        alias = request.POST.get
        return render (request, 'form.html')
