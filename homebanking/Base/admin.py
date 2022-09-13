from django.contrib import admin
from .models import *


# Register your models here.
class ContactEmpleado(admin.ModelAdmin):
    readonly_fields: ('created')

admin.site.register(Empleado,ContactEmpleado)


admin.site.register(Movimientos)