#forms.py
from django import forms

class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)


class GeoForm(forms.Form):
	upperLat = forms.DecimalField(max_digits=20, decimal_places=10)
	upperLong = forms.DecimalField(max_digits=20, decimal_places=10)
	lowerLat = forms.DecimalField(max_digits=20, decimal_places=10)
	lowerLong = forms.DecimalField(max_digits=20, decimal_places=10)
	levelOfDetail = forms.IntegerField()

