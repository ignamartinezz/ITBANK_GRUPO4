from rest_framework import permissions
from .models import Empleado
from Clientes.models import Cliente

class isEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        return list(Empleado.objects.filter(employee_dni=username)) != []