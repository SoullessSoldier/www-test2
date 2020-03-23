from django.contrib import admin

# Register your models here.
from .models import Clients,Staff,Form_education,Employee
admin.site.register(Clients)
admin.site.register(Staff)
admin.site.register(Form_education)
admin.site.register(Employee)
