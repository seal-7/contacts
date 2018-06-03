from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.index),
	path('user/',include('user.urls')),
	path('phonebook/',include('phonebook.urls')),
    path('admin/', admin.site.urls),
]
