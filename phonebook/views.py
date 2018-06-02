from django.shortcuts import render
from django.http import HttpResponse
from .controller import *
from user.controller import *
# Create your views here.

def add(request):
	if(request.method == 'POST'):
		#POST
		data_to_store={
			'user' : request.POST.get('user',''),
			'contactName' : request.POST.get('contactName',''),
			'contacts' : request.POST.get('contacts','').split(',')			
		}
		print(data_to_store)
		user = addContact(data_to_store)
		response = HttpResponse(str(user))
	else:
		#GET
		all_users = getAllUsers()
		response = render(request,'phonebook/add.html',{'users':all_users})
	return response