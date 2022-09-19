from django.shortcuts import render, redirect
from .models import Administrador, Empleado, Medicamento, Proveedor

def home(request):
    return render(request, "g_principal.html")

def pag_principal(request):
    return render(request, "g_principal.html")

def empleado(request):
    empleado = Empleado.objects.all()
    return render(request, "g_empleados.html",{"Empleados": empleado})

def administrador(request):
    administrador = Administrador.objects.all()
    return render(request, "g_administrador.html", {"Administradores": administrador})

def proveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, "g_proveedor.html", {"Proveedores": proveedor})

def medicamentos(request):
    medicamento = Medicamento.objects.all()
    return render(request, "g_medicamento.html", {"Medicamento": medicamento})

def registroempleado(request):
    id = request.POST['numid']
    nombres = request.POST['txtNombres']
    apellidos = request.POST['txtApellidos']
    telefono = request.POST['numTelefono'] 
    cargo = request.POST['txtCargo']

    Empleados = Empleado.objects.create(id=id, nombres=nombres, apellidos=apellidos, telefono=telefono, cargo=cargo)
    return redirect('/g_empleados.html')

def registroadministrador(request):
    nombres = request.POST['txtNombres']
    apellidos = request.POST['txtApellidos']
    codigo = request.POST['numCodigo']
    telefono = request.POST['numTelefono']

    Administardores = Administrador.objects.create(nombres=nombres, apellidos=apellidos, codigo=codigo, telefono=telefono)
    return redirect('/g_administrador.html')

def registroproveedor(request):
    nombre_proveedor=request.POST['txtNombre']
    ruc = request.POST['numRuc']
    telefono = request.POST['numTelefono']
    direccion = request.POST['txtDireccion']

    Proveedores = Proveedor.objects.create(nombre_proveedor=nombre_proveedor, ruc=ruc, telefono=telefono, direccion=direccion)
    return redirect('/g_proveedor.html')

def registromedicamento(request):
    Tipo = request.POST['txtTipo']
    nombre = request.POST['txtNombre']
    fecha_expiracion = request.POST['numFechaexpiracion']
    fecha_produccion = request.POST['numFechaproduccion']
    precio_Compra = request.POST['numCompra']
    precio_venta = request.POST['numVenta']

    Medicamentos = Medicamento.objects.create(Tipo=Tipo, nombre=nombre, fecha_expiracion=fecha_expiracion, fecha_produccion=fecha_produccion, precio_Compra=precio_Compra, precio_venta=precio_venta)
    return redirect('/g_medicamento.html')
