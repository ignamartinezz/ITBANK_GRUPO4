from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Prestamo
from .forms import  PrestamoForm
from .serializers import PrestamoSerializer
from Clientes.models import Cliente
from Base.models import Sucursal
from Cuentas.models import Cuenta



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

# Create your views here.

class ObtenerPrestamosCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,customer_id):
        cliente=Cliente.objects.filter(customer_dni=str(customer_id)).first()
        if cliente.exists():
            listaprestamo=Prestamo.objects.filter(customer_id=cliente.customer_id)
            serializer=PrestamoSerializer(listaprestamo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class ObtenerPrestamosSucursal(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, sucursal_id):
        clientela= Cliente.objects.filter(branch_id=sucursal_id)
        listaprestamos=[]
        for cliente in clientela:
            if Prestamo.objects.filter(customer_id=cliente.customer_id).exists():
                listaprestamos.extend(list(Prestamo.objects.filter(customer_id=cliente.customer_id)))
        if listaprestamos:
            serializer= PrestamoSerializer(listaprestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class DeletePrestamo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self,request,loan_id):
        prestamo=Prestamo.objects.filter(loan_id=loan_id).first()
        if prestamo:
            serializer=PrestamoSerializer(prestamo)
            cuentacliente=Cuenta.objects.get(customer_id=serializer.data["customer_id"])
            cuentacliente.balance+=serializer.data["loan_total"]
            cuentacliente.save()
            prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class CrearPrestamo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        data['loan_date']= date.today().strftime('%Y-%m-%d')
        serializer=PrestamoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_200_OK)


@login_required(login_url='login')
def prestamo(request):
    form=PrestamoForm
    context={
        'form':form
    }
    
    if request.method=="POST":
        form=form(data=request.POST)
        if form.is_valid():
            loan_typeData=request.POST.get('loan_type','')
            loan_dateData=request.POST.get('loan_date','')
            loan_totalData=request.POST.get('loan_total','')
    
            prestamo=Prestamo(loan_type=loan_typeData,loan_date=loan_dateData
            ,loan_total=loan_totalData,customer_id=1)
            prestamo.save()
            return redirect(reverse('homeBanking'))
    return render(request, "Prestamos/prestamo.html", context)
