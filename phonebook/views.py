from django.shortcuts import render, redirect
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
			'contacts' : request.POST.get('email','').split(',') + request.POST.get('phone','').split(',')			
		}				
		addContact(data_to_store)
		response = render(request,'phonebook/add.html',{'users':getAllUsers(),'message':'Contact Added succesfully!','type':'success'})

	else:
		#GET
		users = getAllUsers()
		if users == []:
			response = render(request,'phonebook/add.html',{'users':users,'message':'Create User First','type':'error'})
		else:
			response = render(request,'phonebook/add.html',{'users':users})
	return response

def merge(request):
	if(request.method == 'POST'):
		#POST
		merge_list = getMergeList(request.POST.get('user',''))
		return render(request,'phonebook/mergeList.html',{'mergeList':str(merge_list)})
	else:
		#GET
		response = render(request,'phonebook/merge.html',{'users':getAllUsers()})

	return response