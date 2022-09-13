from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Clientes.serializers import ClienteSerializer
from Clientes.models import Cliente
from .models import Tarjeta
from .serializers import TarjetaSerializer


# Create your views here.

class ObtenerTarjetasCliente(APIView):
    def get(self,request,customer_id):
        cliente=Cliente.objects.filter(customer_dni=str(customer_id)).first()
        if cliente.exists():
            tarjetas=Tarjeta.objects.filter(customer_id=cliente.customer_id)
            serializer=TarjetaSerializer(tarjetas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    