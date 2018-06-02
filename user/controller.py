from .models import CreateUser
from phonebook.models import *

def setUser(userName):
	user = CreateUser.objects.filter(name=userName)
	if not user:		
		user = CreateUser(name=userName, data={})		
		user.save()
		PhoneToContactMap(name=userName, data={}).save()
		EmailToContactMap(name=userName, data={}).save()
	else:
		user = "USER ALREADY EXIST"
	return user

def getAllUsers():	
	users = []
	users_from_db = CreateUser.objects.all()
	for user in users_from_db:
		users.append(user.name)
	return users

def getUser(userName):
	return CreateUser.objects.filter(name=userName)	