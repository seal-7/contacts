from .models import *
from user.models import CreateUser
from .UnionFind import UnionFind
def addContact(data_to_store):
	
	user = CreateUser.objects.filter(name=data_to_store['user'])[0]
	user.data[data_to_store['contactName']] = data_to_store['contacts']	
	user.save()

	user_in_phone = PhoneToContactMap.objects.filter(name=data_to_store['user'])[0]
	user_in_email = EmailToContactMap.objects.filter(name=data_to_store['user'])[0]
	
	for contact in data_to_store['contacts']:
		if(contact != ''):
			if('@' in contact):
				#replace the above condition with if('e' in contact):
				#email
				if not user_in_email.data.get(contact):
					user_in_email.data[contact] = []

				user_in_email.data[contact].append(data_to_store['contactName'])
				
					
			else:
				if not user_in_phone.data.get(contact):
					user_in_phone.data[contact] = []
				user_in_phone.data[contact].append(data_to_store['contactName'])
	
	user_in_phone.save()
	user_in_email.save()				

def getMergeList(userName):

	contact_map = CreateUser.objects.filter(name=userName)[0].data
	phone_map = PhoneToContactMap.objects.filter(name=userName)[0].data
	email_map = EmailToContactMap.objects.filter(name=userName)[0].data

	U = UnionFind()

	for phone in list(phone_map.keys()):
			if(len(phone_map[phone]) > 1):
				for contact in phone_map[phone][1:]:
					U.union(phone_map[phone][0],contact)

	for email in list(email_map.keys()):
			if(len(email_map[email]) > 1):
				for contact in email_map[email][1:]:
					U.union(email_map[email][0],contact)

	ans = {}

	for contact in list(contact_map.keys()):
		key = U.__getitem__(contact)

		if not ans.get(key):	
			ans[key] = []

		ans[key].append(contact)

	return str(list(ans.values()))