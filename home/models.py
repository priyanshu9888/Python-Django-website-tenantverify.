from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


# Create your models here.
PURPOSE_CHOICE=(
    ('Complaint','Complaint'),
    ('Business Enquiry', 'Business Enquiry'),
)
GENDERC=(
    ('male','male'),
    ('female','female'),
)
MARTIAL=(

    ('Married','Married'),
    ('Unmarried','Unmarried'),
)

class Apointment(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    option=models.TextField(PURPOSE_CHOICE)
    desc = models.TextField()
    msg=models.TextField()
def __str__(self):
        return self.name
   


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()

def __str__(self):
        return self.name

class Tdata(models.Model):
    fullname =models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    placeofbirth = models.CharField(max_length=200)
    dateofbirth = models.DateField(auto_now=False,auto_now_add=False)

    gender = models.TextField(GENDERC)
    martial = models.TextField(MARTIAL)
    nationality = models.CharField(max_length=12)
    language = models.TextField(max_length=100) 
    contactnum = models.CharField(max_length=10)
    contactnum2 = models.CharField(max_length=10)
    
    adhar = models.CharField(max_length=12)
    Linkno = models.CharField(max_length=10)
    Occupation = models.CharField(max_length=100)
    nameofcompany = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    ownerno = models.CharField(max_length=10)
    socityname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    namestay = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    numb = models.CharField(max_length=10)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    state = models.CharField(max_length=14)
    pincode = models.PositiveIntegerField()
    police = models.CharField(max_length=100)
    period = models.CharField( max_length=10)
    presentsameperma =models.TextField(max_length=10)
    peraddress = models.CharField(max_length=100)
    pervillcity = models.CharField(max_length=100)
    state2 = models.CharField(max_length=12)
    pincode2 = models.PositiveIntegerField()

    police2 = models.CharField(max_length=100)
    period2 = models.CharField(max_length=10)
    image = models.ImageField(upload_to="formimage")
    document = models.FileField(upload_to="file")
        	
def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)