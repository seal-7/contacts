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
			'contacts' : request.POST.get('contacts','').split(',')			
		}		
		user = addContact(data_to_store)
		response = redirect('/phonebook/add/')
	else:
		#GET
		response = render(request,'phonebook/add.html',{'users':getAllUsers()})
	return response

def merge(request):
	if(request.method == 'POST'):
		merge_list = getMergeList(request.POST.get('user',''))
		return HttpResponse(merge_list)
	else:
		#GET
		response = render(request,'phonebook/merge.html',{'users':getAllUsers()})

	return response