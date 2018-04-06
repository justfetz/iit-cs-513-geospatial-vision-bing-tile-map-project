"""stockRoller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from first_app import views
from django.conf.urls import include

urlpatterns = [

	path('first_app/', include('first_app.urls')),
	path('', views.GeoViewForm, name='index'),
    path('admin/', admin.site.urls),
    path('map', views.map, name='map'),
   # path('inventory', views.inventory, name='inventory'),
   # path('base', views.base, name='base'),
   # path('base2', views.base2, name='base2'),
    path('forms', views.form_name_view, name='form'),
    path('geo', views.GeoViewForm, name='geo'),
    path('about', views.about, name='about')
    #projections $ orders form
    

]
