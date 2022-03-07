from django.contrib import admin
from .models import Company, Customer, Department, Employee, ServiceItem, Supplier, Client

# Register your models here.

# admin.site.register(User)
admin.site.register(Company)
admin.site.register(ServiceItem)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Department)