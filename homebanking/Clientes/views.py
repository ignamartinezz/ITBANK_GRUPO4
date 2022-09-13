from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

from Cuentas.serializers import CuentaSerializer
from Cuentas.models import Cuenta
from .models import Cliente
from .serializers import ClienteSerializer

# Create your views here.

class ObtenerDatosCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,customer_id):
        cliente=Cliente.objects.filter(customer_dni=str(customer_id)).first()
        if cliente.exists():
            datoscliente=Cliente.objects.filter(customer_id=cliente.customer_id)
            serializer=ClienteSerializer(datoscliente, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
     
class ObtenerSaldoCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,customer_id):
        cliente=Cliente.objects.filter(customer_dni=str(customer_id)).first()
        if cliente.exists():
            cuentacliente=Cuenta.objects.filter(customer_id=cliente.customer_id)
            serializer=CuentaSerializer(cuentacliente, many=True)
            return Response(serializer.data["balance"], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
     