from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Prestamo
from .forms import  PrestamoForm

# Create your views here.

@login_required(login_url='login')
def prestamo(request):
    form=PrestamoForm(data=request.POST)
    
    


    context={
        'form':form
    }
#    context['form']=PrestamoForm(data=request.POST)
    
    
    return render(request, "Prestamos/prestamo.html", context)


# def prestamo(request):
#     return render(request, "Prestamos/prestamo.html")
