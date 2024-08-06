from django.contrib import admin
from .models import Register,FailedLoginAttempts

class AdminRegister(admin.ModelAdmin):
    list_display =('person_name','phone_no','purpose_of_visit','visite_time','return_time','visit_id')
    list_filter=('person_name','phone_no','purpose_of_visit','visite_time','return_time','visit_id')
    search_fields=('person_name','phone_no','purpose_of_visit','visite_time','return_time','visit_id')

class FailedLoginAttemptsAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'attempts', 'is_active')
    list_filter = ('device_id', 'attempts', 'is_active')
    search_fields = ('device_id', 'attempts', 'is_active')

admin.site.register(FailedLoginAttempts, FailedLoginAttemptsAdmin)
admin.site.register(Register,AdminRegister)
