from django.contrib import admin
from django.urls import path
from qrapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adminlogin,name='adminlogin'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('adminscan/',views.adminscan,name='adminscan'),
    path('createvisitor/',views.createvisitor,name='createvisitor'),
]
