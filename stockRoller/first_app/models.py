from django.db import models



class Topic(models.Model):
	top_name= models.CharField(max_length=264, unique=True)


	def __str__(self):
		return self.top_name

class WebPage(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
	date = models.DateField()
	

	def __str__(self):
		return str(self.date)


class RollStock(models.Model):
	width = models.IntegerField()
	paperType = models.CharField(max_length=264, unique=True)
	lineal = models.IntegerField()
	weight = models.DecimalField(decimal_places=3, max_digits=10)
	quantity = models.DecimalField(decimal_places=3, max_digits=10)

	def __str__(self):
		return str(self.quantity, self.paperType)

class order(models.Model):
	#id
	#workDays per month
	#width
	#type
	#quantity
	#orderRecord
	pass

class User(models.Model):
	firstname = models.CharField(max_length=264, unique=True)
	lastname = models.CharField(max_length=264, unique=True)
	email = models.CharField(max_length=264, unique = True)

	def __str__(self):
		return str(self.email)

		

	#user, firstname, lastname, email
	#populate fake user, create view, html, list of names
	#template tags





# Create your models here.
