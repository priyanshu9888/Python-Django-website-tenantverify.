from django.db import models

# Create your models here.
PURPOSE_CHOICE=(
    ('Complaint','Complaint'),
    ('Business Enquiry', 'Business Enquiry'),
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


        	
