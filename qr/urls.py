from django.contrib import admin
from django.urls import path
from qrapp import views
from django.conf.urls import handler404
from django.shortcuts import render
from django.http import HttpResponseNotFound 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('',views.adminpage,name='adminpage'),
    path('update_time/',views.update_time,name='update_time'),
    path('adminvisitors/',views.adminvisitors,name='adminvisitors'),
    path('get_visitors/',views.get_visitors,name='get_visitors'),
    path('adminscan/',views.adminscan,name='adminscan'),
    path('adminlogout/',views.admin_logout_view,name='adminlogout'),
    path('createvisitor/',views.createvisitor,name='createvisitor'),
    path('downloadreport/',views.download_overall_report,name='downloadreport'),
]
def custom_page_not_found_view(request, exception):
    print("404 handler reached1.") 
    return HttpResponseNotFound(render(request, '404.html')) 

handler404 = custom_page_not_found_view