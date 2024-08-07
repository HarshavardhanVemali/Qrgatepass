from django.contrib import admin
from django.urls import path
from qrapp import views
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
]
