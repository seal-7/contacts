from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(request):
	if(request.method == 'POST'):
		#POST
		jsonData={
			'user' : request.POST.get('user',''),
			'contactName' : request.POST.get('contactName',''),
			'contacts' : str(request.POST.get('contacts','').split(','))			
		}
		print(jsonData)
		response = HttpResponse(str(jsonData))
	else:
		#GET
		response = render(request,'phonebook/add.html',{'users':['raj','imran']})
	return response