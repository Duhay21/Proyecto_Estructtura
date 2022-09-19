from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.IntegerField(primary_key=True,max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=10) 
    cargo = models.CharField(max_length=50)

    def __str__(self):
      texto ="{0} ({1})"
      return texto.format( self.nombres, self.apellidos, self.id,  self.telefono, self.cargo)


class Administrador(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    codigo = models.IntegerField(primary_key=True, max_length=6)
    telefono = models.IntegerField(max_length=10) 


    def __str__(self):
      texto ="{1} ({2})"
      return texto.format(self.codigo, self.nombres, self.apellidos, self.telefono)


class Proveedor(models.Model):	
	nombre_proveedor = models.CharField(max_length=30)	
	ruc = models.CharField(unique=True, max_length=10)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=60)

         
class Medicamento(models.Model):
	TIPO = (
        ('generico', 'Generico'),
        ('laboratorio', 'Laboratorio'),
    )
	Tipo = models.CharField(choices=TIPO, max_length=30)
	nombre = models.CharField(max_length=200, unique=True)
	fecha_expiracion = models.DateField()
	fecha_produccion = models.DateField()	
	precio_Compra = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	precio_venta = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)