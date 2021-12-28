from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView 
# from home.admin import ApointmentAdmin
from .models import Apointment
from .models import Contact
from .models import Tdata  
from django.contrib import messages 
from .forms import UserRegistrationForm,UserProfileForm
from .models import Profile
import requests 
from django.contrib.auth.hashers import make_password
import random
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

#         # Create your views here.


def userprofile(request):
   return render(request, 'users/index.html') 

def index(request):
   return render(request, 'home/index.html')

def start(request):
     return render(request, 'start/index.html')

def apointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        option=request.POST.get('option')
        apointment=Apointment(name=name,email=email, phone=phone,desc=desc,option=option)
        apointment.save()
        messages.success(request, '	Thank you for contacting us, we will get back to you shortly.')        
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
        messages.success(request, 'Contact form submited successfully we will get back to you shortly.')        
        return redirect("contact")
    return render(request,"contact/index.html")

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about/index.html')

def cancel(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service/index.html')

def privacy(request):
    return render(request,'privacy/index.html' )

def termsandcondition(request):
    return render(request,'terms/index.html')

def disclaimer(request):
    return render(request,'disclaimer/index.html')

def media(request):
    return render(request, 'media/index.html')

def tdata(request):
    return render (request, '/tdata.html')

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
        image1=request.FILES ['image1']
        image2=request.FILES ['image2']

        image3=request.FILES ['image3']
        image4=request.FILES ['image4']

        # document=request.FILES ['document']

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
        image1=image1,image2=image2,image3=image3,image4=image4,)
        # tdata = (request.POST, request.FILES)
       
        tdata.save()
        messages.success(request, ' form submited successfully')        
       
        return redirect("tdata")
    return render (request, 'tdata.html')

def send_otp(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    # url=" https://2Factor.in"
    api = "JUcNMR548eW6MI1lzvIEHyRVmJMxVzl8glD8TpS1ovC39BEKLcB44CZr8k1R"
    querystring = {"authorization":api,"sender_id":"FTWSMS","message":message,"language":"english","route":"p","numbers":number}
    headers = {
        'cache-control': "no-cache"
    }
    return requests.request("GET", url, headers=headers, params=querystring)

def Registration(request):
    if request.method == "POST":
        fm = UserRegistrationForm(request.POST)
        up = UserProfileForm(request.POST)
        if fm.is_valid() and up.is_valid():
            e = fm.cleaned_data['email']
            u = fm.cleaned_data['username']
            p = fm.cleaned_data['password1']
            request.session['email'] = e
            request.session['username'] = u
            request.session['password'] = p
            p_number = up.cleaned_data['phone_number']
            request.session['number'] = p_number
            otp = random.randint(1000,9999)
            request.session['otp'] = otp
            message = f'Use OTP{otp} to login to your Account Tenantvrify.in does not ask for OTP or Contact number to be shared with anyone including Tenantverify Personnel. '
            send_otp(p_number,message)
        return redirect('/registration/otp/')
    else:
        fm  = UserRegistrationForm()
        up = UserProfileForm()
    context = {'fm':fm,'up':up}
    return render(request,'login/signup.html',context)


def otpRegistration(request):
    if request.method == "POST":
        u_otp = request.POST['otp']
        otp = request.session.get('otp')
        user = request.session['username']
        hash_pwd = make_password(request.session.get('password'))
        p_number = request.session.get('number')
        email_address = request.session.get('email') 

        if int(u_otp) == otp:
            User.objects.create(
                            username = user,
                            email=email_address,
                            password=hash_pwd
            )
            user_instance = User.objects.get(username=user)
            Profile.objects.create(
                            user = user_instance,phone_number=p_number
            )
            request.session.delete('otp')
            request.session.delete('user')
            request.session.delete('email')
            request.session.delete('password')
            request.session.delete('phone_number')

            messages.success(request,'Registration Successfully Done !!')

            return redirect('/login/')
        
        else:
            messages.error(request,'Wrong OTP')


    return render(request,'login/signup-otp.html')


def userLogin(request):
    template = "login/signin.html"
    try :
        if request.session.get('failed') > 2:
            return HttpResponse('<h1> You have to wait for 5 minutes to login again</h1>')
    except:
        request.session['failed'] = 0
        request.session.set_expiry(1000)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect("start")
            else:
                request.session['username'] = username
                request.session['password'] = password
                u = User.objects.get(username=username)
                p = Profile.objects.get(user=u)
                p_number = p.phone_number
                otp = random.randint(1000,9999)
                request.session['login_otp'] = otp
                message = f'your Tenantverify.in otp is {otp}'
                send_otp(p_number,message)
                return redirect('/login/otp/')
        else:
            messages.error(request,'username or password is wrong')
        # return render(request,'login.html')
    # elif request.method == "GET":
    #     print("!!!!!! {}".format(request))
    #     if request.session is not None:
    #         username = request.session['username']
    #         password = request.session['password']
    #         user = authenticate(request,username=username,password=password)
    #         if user is not None:
    #             django_login(request, user)
    #             return redirect("start")

    return render(request,template)


def otpLogin(request):
    if request.method == "POST":
        username = request.session['username']
        password = request.session['password']
        otp = request.session.get('login_otp')
        u_otp = request.POST['otp']
        if int(u_otp) == otp:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                request.session.delete('login_otp')
                messages.success(request,'login successfully')
                return redirect('start.html')
        else:
            messages.error(request,'Wrong OTP')
    return render(request,'login/login-otp.html')

def home(request):
    if request.method == "POST":
        otp = random.randint(1000,9999)
        request.session['email_otp'] = otp
        message = f'your otp is {otp}'
        user_email = request.user.email

        send_mail(
            'Email Verification OTP',
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
        return redirect('/email-verify/')

    return render(request,'start.html')

def email_verification(request):
    if request.method == "POST":
        u_otp = request.POST['otp']
        otp = request.session['email_otp']
        if int(u_otp) == otp:
           p =  Profile.objects.get(user=request.user)
           p.email_verified = True
           p.save()
           messages.success(request,f'Your email {request.user.email} is verified now')
           return redirect('/start.html')
        else:
            messages.error(request,'Wrong OTP')


    return render(request,'email-verified.html')

def forget_password(request):
    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            uid = User.objects.get(email=email)
            url = f'http://127.0.0.1:8000/change-password/{uid.profile.uuid}'
            send_mail(
            'Reset Password',
            url,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
            return redirect('/forget-password/done/')
        else:
            messages.error(request,'email address is not exist')
    return render(request,'login/forget-password.html')

def change_password(request,uid):
    try:
        if Profile.objects.filter(uuid = uid).exists():
            if request.method == "POST":
                pass1 = 'password1'in request.POST and request.POST['password1']
                pass2 =  'password2'in request.POST and request.POST['password2']
                if pass1 == pass2:
                    p = Profile.objects.get(uuid=uid)
                    u = p.user
                    user = User.objects.get(username=u)
                    user.password = make_password(pass1)
                    user.save()
                    messages.success(request,'Password has been reset successfully')
                    return redirect('/login/')
                else:
                    return HttpResponse('Two Password did not match')
                
        else:
            return HttpResponse('Wrong URL')
    except:
        return HttpResponse('Wrong URL')
    return render(request,'change-password.html')