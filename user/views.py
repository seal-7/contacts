from django.shortcuts import render
from django.http import HttpResponse
from .controller import *

def create(request):	
	if(request.method == 'POST'):
		message = setUser( str(request.POST.get('userName','')) )
		response = render(request,'user/create.html',message)
	else:		
		response = render(request,'user/create.html',{})
	return response

def delete(request):
	if(request.method == 'POST'):
		message = removeUser( str(request.POST.get('userName','')) )
		response = render(request,'user/delete.html',message)
	else:		
		users = getAllUsers()
		if users == []:
			response = render(request,'user/delete.html',{'users':users,'message':'Create User first','type':'error'})
		else:
			response = render(request,'user/delete.html',{'users':users})
	return response