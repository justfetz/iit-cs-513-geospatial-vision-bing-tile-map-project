from django.conf.urls import url
from first_app import views
from django.urls import path

urlpatterns = [
	path('',views.GeoViewForm, name='geo'),
	path('about', views.about, name='about')

]