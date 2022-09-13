from django.contrib import admin
from django.urls import path
from Base import views as baseView
from Prestamos import views as PrestamoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',   baseView.home, name="home"),
    path('signup/', baseView.login, name="login"),
    path('signup/homeBanking', baseView.homeBanking, name="homeBanking"),
    path('homeBanking/', baseView.homeBanking, name="homeBanking"),
    path('prestamo/', PrestamoView.prestamo, name="prestamo"),
    
]

