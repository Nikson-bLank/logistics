from django.contrib import admin

from .models import Driver_Detail
# Register your models here.
from django.contrib.messages import constants as messages
from . import models 
# Register your models here.

class DriverAdminArea(admin.AdminSite):
    site_header= 'Logistics'

class TestAdminPermissions(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone_number','address']
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        if request.POST.get('action') == 'change_selected':
            messages.add_message(request,messages.ERROR,(
                "i really hope you are sure about this!"
            ))
        return True
    
    def has_delete_permission(self, request, obj=None):
        # if request.POST.get('action') == 'delete_selected':
        #     messages.add_message(request,messages.ERROR,(
        #         "i really hope you are sure about this!"
        #     ))
        return True
    
    def has_view_permission(self, request,obj= None):
        return True


driver_site = DriverAdminArea(name='DriverAdmin')
driver_site.register(models.Driver_Detail, TestAdminPermissions)

@admin.register(Driver_Detail)
class Driver_DetailAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone_number','address']