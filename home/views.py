from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from home.admin import ApointmentAdmin

from .models import Apointment
from .models import Contact
from .models import Tdata
from django.contrib.auth import authenticate, login
from django.conf import settings
import http.client
import random
from .models import Profile
from django.contrib.auth.models import User





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


def tdata(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        alias = request.POST.get('alias')
        father = request.POST.get('father')
        placeofbirth = request. POST.get('placeofbirth')
        dateofbirth = request.POST.get('dateofbirth')
        gender = request.POST.get('gender')
        martial = request.POST.get('martial')
        nationality = request.POST.get('nationality')
        language = request.POST.get('language')
        contactnum = request.POST.get('contactnum')
        contactnum2 = request.POST.get('contactnum2')
        adhar = request.POST.get('adhar')
        Linkno = request.POST.get('Linkno')
        Occupation = request.POST.get('Occupation')
        nameofcompany = request.POST.get('nameofcompany')
        ownername = request.POST.get('ownername')
        ownerno = request.POST.get('ownerno')
        socityname = request.POST.get('socityname')
        address = request.POST.get('address')
        namestay = request.POST.get('namestay')
        relationship = request.POST.get('relationship')
        numb = request.POST.get('numb')
        address2 = request.POST.get('address2')
        address3 = request.POST.get('address3')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        police = request.POST.get('police')
        period = request.POST.get('period')
        presentsameperma = request.POST.get('presentsameperma')
        peraddress = request.POST.get('peraddress')
        pervillcity = request.POST.get('pervillcity')
        state2 = request.POST.get('state2')
        pincode2 = request.POST.get('pincode2')
        police2 = request.POST.get('police2')
        period2 = request.POST.get('period2')
        image = request.POST.get('image')
        document = request.POST.get('document')

        tdata=Tdata(fullname=fullname,alias=alias, father=father,
        placeofbirth=placeofbirth,dateofbirth=dateofbirth,
        gender=gender,martial=martial,nationality=nationality,
        language=language,contactnum=contactnum,contactnum2=contactnum2,
        adhar=adhar,Linkno=Linkno,Occupation=Occupation,
        nameofcompany=nameofcompany,ownername=ownername,
        ownerno=ownerno,socityname=socityname,address=address,
        namestay=namestay,relationship=relationship,numb=numb,
        address2=address2,address3=address3,state=state,
        pincode=pincode, police=police, period=period, presentsameperma=presentsameperma,
        peraddress=peraddress,pervillcity=pervillcity,state2=state2,pincode2=pincode2,
        
        police2=police2,period2=period2,
        image=image,document=document)
        tdata.save()
        messages.success(request, ' form submited successfully')        
       
        return redirect("tdata")
    return render (request, 'tdata.html')

#send otp through api call---------------------------------------------------------
def send_otp(mobile , otp):
    print("FUNCTION CALLED")
    conn = http.client.HTTPSConnection("api.2factor")
    authkey = settings.AUTH_KEY 
    headers = { 'content-type': "application/json" }
    url = " https://2factor.in/API/V1/{75b57500-13ea-11e9-9ee8-0200cd936042}/BAL/SMS   ="+otp+"&message="+"Your otp is "+otp +"&mobile="+mobile+"&authkey="+authkey+"&country=91"
    conn.request("GET", url , headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    return None
#login attempt--------------------------------------------------------------------------------------------------
def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        
        user = Profile.objects.filter(mobile = mobile).first()
        
        if user is None:
            context = {'message' : 'User not found' , 'class' : 'danger' }
            return render(request,'login.html' , context)
        
        otp = str(random.randint(1000 , 9999))
        user.otp = otp
        user.save()
        send_otp(mobile , otp)
        request.session['mobile'] = mobile
        return redirect('login_otp')        
    return render(request,'login.html')

#login otp------------------------------------------------------------------------------------------------------
def login_otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            user = User.objects.get(id = profile.user.id)
            login(request , user)
            return redirect('tdata')
        else:
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'login_otp.html' , context)
    
    return render(request,'login_otp.html' , context)

#register------------------------------------------------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        
        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(mobile = mobile).first()
        
        if check_user or check_profile:
            context = {'message' : 'User already exists' , 'class' : 'danger' }
            return render(request,'register.html' , context)
            
        user = User(email = email , first_name = name)
        user.save()
        otp = str(random.randint(1000 , 9999))
        profile = Profile(user = user , mobile=mobile , otp = otp) 
        profile.save()
        send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('otp')
    return render(request,'register.html')

def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            return redirect('tdata')
        else:
            print('Wrong')
            
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'otp.html' , context)
            
        
    return render(request,'otp.html' , context)