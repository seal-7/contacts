from django.contrib import admin
from .models import PhoneToContactMap, EmailToContactMap

# Register your models here.
admin.site.register(PhoneToContactMap)
admin.site.register(EmailToContactMap)