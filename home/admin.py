from django.contrib import admin

from home.models import Apointment 
from home.models import Contact
# from home.views import Apointment, contact

# Register your models here.

class ApointmentAdmin(admin.ModelAdmin):
    list_display=('name', 'phone','email','option','desc')
admin.site.register(Apointment , ApointmentAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','desc', )
admin.site.register(Contact , ContactAdmin)
