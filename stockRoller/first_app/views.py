from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
from . import forms
import math
from . import tilePython


# Create your views here.

def index(request):
	#return render(request, 'first_app/templates/helloHTML.html')
	webPageList = AccessRecord.objects.order_by('date')
	my_dict = {'insert_me':"Hello Insertion, now I am in first_app"}
	date_dict = {'access_records':webPageList}
	#return HttpResponse("Hello There stockroller!")
	return render(request, "first_app/index.html", context = date_dict)

def map(request):
	return render(request, 'first_app/map.html')

#def inventory(request):
#	return render(request, 'first_app/inventory.html')

#def base(request):
#	return render(request, 'first_app/base.html')

def form_name_view(request):
	form = forms.FormName()
	return render(request, 'first_app/forms.html', {'form':form})

def GeoViewForm(request):
	#hello = TileSystem()


	form = forms.GeoForm()
	return render(request, 'first_app/geo.html', {'form':form})
	#class Meta:


#def base2(request):
#	return render(request, 'first_app/base2.html')

def about(request):
	return render(request, 'first_app/about.html')

