from django.contrib import admin

# Register your models here.

from .models import	Pais, Cliente

admin.site.register(Pais)
admin.site.register(Cliente)