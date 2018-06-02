from django.shortcuts import render
from django.http import HttpResponse
from .controller import *

def create(request):	
	if(request.method == 'POST'):
		user = setUser( str(request.POST.get('userName','')) )
		response = HttpResponse(str(user))
	else:		
		response = render(request,'user/create.html',{})
	return response