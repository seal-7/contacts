from .models import CreateUser
from phonebook.models import *

def setUser(userName):
	user = CreateUser.objects.filter(name=userName)
	message = {}
	if not user:		
		user = CreateUser(name=userName, data={})		
		user.save()
		PhoneToContactMap(name=userName, data={}).save()
		EmailToContactMap(name=userName, data={}).save()
		message = { 'message' : "USER CREATED SUCCESFULLY",
		'type' : 'success'
		}
	else:
		message = { 'message' : "USER ALREADY EXIST",
		'type' : 'error'
		}

	return message

def removeUser(userName):
	user = CreateUser.objects.filter(name=userName)
	user_in_phonebook = PhoneToContactMap.objects.filter(name=userName)
	user_in_emailbook = EmailToContactMap.objects.filter(name=userName)
	print(userName)
	print(user)
	print(user_in_phonebook)
	print(user_in_emailbook)
	user.delete()
	user_in_phonebook.delete()
	user_in_emailbook.delete()
	return {'message':'User Deleted Succesfully','type':'success'}

def getAllUsers():	
	users = []
	users_from_db = CreateUser.objects.all()
	for user in users_from_db:
		users.append(user.name)
	return users

def getUser(userName):
	return CreateUser.objects.filter(name=userName)	