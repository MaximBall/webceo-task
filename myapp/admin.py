from django.contrib import admin
from .models import Employee, Item, Sale, ChangePrice

admin.site.register(Employee)
admin.site.register(Item)
admin.site.register(Sale)
admin.site.register(ChangePrice)