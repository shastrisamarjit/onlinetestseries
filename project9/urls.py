"""project9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app9 import views
from project9 import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.show,name="main"),
    path('registerpage/', views.showregister,name="registerpage"),
    path('adminpage/',views.showadmin,name="adminpage"),
    path('facultypanel/',views.showfaculty,name="facultypanel"),
    path('savecourse/',views.savecourse,name="savecourse"),
    path('saveregister/',views.saveregister,name="saveregister"),
    path('checklogin/',views.checklogin,name="checklogin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminpanel/',views.adminpanel,name="adminpanel"),
    path('showadmin/',views.showadminpage,name="showadminpage"),
    path('viewall/',views.viewall,name="viewall"),
    path('deletest/',views.deletestudent,name="deletestudent"),
    path('coursedelete/',views.coursedelete,name="coursedelete"),
    path('removed/',views.removed,name="removed"),
    path('logout/',views.logout,name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#the above path('registerpage/') will not be able to provide path 
#because html page(testseries2.html) requesting server((using click on a button)way)
#has not used the "{% csrf_token %}" tag after the "<form action=''>"tag
  

