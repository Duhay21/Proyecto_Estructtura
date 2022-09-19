from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('g_principal.html', views.pag_principal),
    path('g_empleados.html', views.empleado),
    path('g_administrador.html', views.administrador),
    path('g_proveedor.html', views.proveedor),
    path('g_medicamento.html', views.medicamentos),
    path('registroempleado/', views.registroempleado),
    path('registroadministrador/', views.registroadministrador),
    path('registroproveedor/', views.registroproveedor),
    path('registromedicamento/', views.registromedicamento)


]