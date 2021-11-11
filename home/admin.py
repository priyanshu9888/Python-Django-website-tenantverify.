from django.contrib import admin

from home.models import Apointment 
from home.models import Contact
from home.models import Tdata
from import_export.admin import ImportExportModelAdmin
from home.models import Profile
# from home.views import Apointment, contact

# Register your models here.

class ApointmentAdmin(admin.ModelAdmin):
    list_display=('name', 'phone','email','option','desc')
admin.site.register(Apointment , ApointmentAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','desc', )
admin.site.register(Contact , ContactAdmin)

class TdataAdmin(ImportExportModelAdmin ,admin.ModelAdmin ):
    list_display=('fullname','alias','father','placeofbirth','dateofbirth',
     'gender','martial','nationality','language','contactnum','contactnum2','adhar',
     'Linkno','Occupation','nameofcompany','ownername','ownerno','socityname',
     'address','namestay','relationship','numb','address2','address3','state',
     'pincode','police','period','presentsameperma','peraddress','pervillcity','state2','pincode2',
     'police2','period2','image','document',)
admin.site.register( Tdata, TdataAdmin)

admin.site.register(Profile)
