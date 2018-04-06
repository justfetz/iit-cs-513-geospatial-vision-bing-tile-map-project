import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockRoller.settings')


import django
django.setup()


import random

from first_app.models import User


from faker import Faker
fakegen= Faker()

def populate(N=5):
	for entry in range(N):
		#top = add_topic()

		fake_firstname = fakegen.name()[0]
		fake_lastname = fakegen.name()[1]
		fake_email = fakegen.email()
		

		namer = User.objects.get_or_create(name= fake_firstname, email=fake_email)

		#webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

		#acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
	print("populating script")
	populate(20)
	print("Pop complete")

