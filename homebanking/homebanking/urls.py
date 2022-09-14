from django.contrib import admin
from django.urls import path
from Base import views as baseView
from Prestamos import views as PrestamoView
from Clientes import views as ClienteView
from Tarjetas import views as TarjetaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',   baseView.home, name="home"),
    path('login/', baseView.login, name="login"),
    path('signup/', baseView.signup, name="signup"),
    
    path('signup/homeBanking', baseView.homeBanking, name="homeBanking"),
    path('homeBanking/', baseView.homeBanking, name="homeBanking"),
    path('prestamo/', PrestamoView.prestamo, name="prestamo"),

    
    
    
    path('api/crear_prestamo/',PrestamoView.CrearPrestamo.as_view(), name="crear_prestamo"),
    path('api/listar_sucursales/',baseView.ListarSucursales.as_view(), name="listar_sucursales"),
    path('api/obtener_prestamos_sucursales/<int:sucursal_id>',PrestamoView.ObtenerPrestamosSucursal.as_view(), name="obtener_prestamos_sucursales"),
    path('api/obtener_prestamos_clientes/<int:customer_id>',PrestamoView.ObtenerPrestamosCliente.as_view(), name="obtener_prestamos_clientes"),
    path('api/delete_prestamo/<int:loan_id>',PrestamoView.DeletePrestamo.as_view(), name="delete_prestamo"),
    path('api/obtener_saldo_cliente/<int:customer_id>',ClienteView.ObtenerSaldoCliente.as_view(), name="obtener_saldo_cliente"),
    path('api/obtener_datos_cliente/<int:customer_id>',ClienteView.ObtenerDatosCliente.as_view(), name="obtener_datos_cliente"),
    path('api/obtener_tarjetas_cliente/<int:customer_id>',TarjetaView.ObtenerTarjetasCliente.as_view(), name="obtener_tarjetas_cliente"),

]

