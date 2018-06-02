from .models import *
from user.models import CreateUser

def addContact(data_to_store):
	
	user = CreateUser.objects.filter(name=data_to_store['user'])[0]
	user.data[data_to_store['contactName']] = data_to_store['contacts']	
	user.save()

	user_in_phone = PhoneToContactMap.objects.filter(name=data_to_store['user'])[0]
	user_in_email = EmailToContactMap.objects.filter(name=data_to_store['user'])[0]
	
	for contact in data_to_store['contacts']:
		if('e' in contact):
			#replace the above condition with if('e' in contact):
			#email
			if not user_in_email.data.get(contact):
				user_in_email.data[contact] = []

			user_in_email.data[contact].append(data_to_store['contactName'])
			
				
		else:
			if not user_in_phone.data.get(contact):
				user_in_phone.data[contact] = []
			user_in_phone.data[contact].append(data_to_store['contactName'])
	
	print(user_in_phone.data)
	print(user_in_email.data)
	user_in_phone.save()
	user_in_email.save()			
	return user.data