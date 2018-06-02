from django.shortcuts import render
from django.http import HttpResponse


def create(request):	
	if(request.method == 'POST'):				
		response = HttpResponse(request.POST.get('userName',''))
	else:		
		response = render(request,'user/create.html',{})
	return response