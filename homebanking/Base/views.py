from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "base/index.html")

def login(request):
    return render(request, "base/signup.html")

def homeBanking(request):
    return render(request, "base/homeBanking.html")