from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegistroForm
from .models import Sucursal
from django.urls import reverse
from django.contrib.auth.models import User, auth

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SucursalSerializer


# Create your views here.

def home(request):
    return render(request, "base/index.html")

def login(request):
    # registro_form = RegistroForm
    # if request.method == "POST":
    #     registro_form = registro_form(data=request.POST)
    #     if registro_form.is_valid():
    #         nombre_user = request.POST.get('registerFirstName', '')
    #         apellido_user = request.POST.get('registerLastName', '')
    #         username_user = request.POST.get('registerUsername', '')
    #         email = request.POST.get('registerEmail', '')
    #         password = request.POST.get('registerPassword', '')
    
    #         user = User.objects.create_user(username_user,email,password)
    #         user.save()

    #         return redirect(reverse('base/signup.html'))
    if request.method == "POST":
        #login
        usernamelogin=request.POST['loginName']
        passwordlogin=request.POST['loginPassword']

        print(usernamelogin)

        usuariologin= auth.authenticate(username=usernamelogin, password=passwordlogin)
        print(usuariologin)

        if usuariologin is not None:
            auth.login(request,usuariologin)
            return redirect('homeBanking')
    return render(request, "base/login.html")




def signup(request):
    registro_form = RegistroForm

    if request.method == "POST":

        registro_form = registro_form(data=request.POST)
                # nombre_user = request.POST.get('registerFirstName', '')
                # print(nombre_user)
        print(registro_form.errors)
        if registro_form.is_valid():
            nombre_user = request.POST.get('registerFirstName', '')
            apellido_user = request.POST.get('registerLastName', '')
            username_user = request.POST.get('registerUsername', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            
            user = User.objects.create_user(username_user, email, password)
            user.first_name=nombre_user
            user.last_name=apellido_user
            user.save()

            return redirect(reverse('login'))
                
    return render(request, "base/signup.html")



@login_required(login_url='login')
def homeBanking(request):
    print(request.user)
    return render(request, "base/homeBanking.html")


class ListarSucursales(APIView):
    
    def get(self,request):
        sucursales= Sucursal.objects.all()
        serializers=SucursalSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)


