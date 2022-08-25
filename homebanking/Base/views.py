from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.urls import reverse
from django.contrib.auth.models import User

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
    registro_form = RegistroForm

    if request.method == "POST":

        registro_form = registro_form(data=request.POST)

        if registro_form.is_valid():
            cliente_id = request.POST.get('cliente_id', '')
            email = request.POST.get('email', '')
            pwd = request.POST.get('pwd', '')
            user = User.objects.create_user(cliente_id, email, pwd)
            user.save()

            return redirect(reverse('login'))
    return render(request, "base/signup.html")

@login_required
def homeBanking(request):
    print(request.user)
    return render(request, "base/homeBanking.html")