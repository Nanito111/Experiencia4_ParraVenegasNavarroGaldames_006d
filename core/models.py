from asyncio.windows_events import NULL
from pyexpat import model
from sqlite3 import Date
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Soporte(models.Model):
    opciones_soporte = [
        [0, "Sugerencia"],
        [1, "Problema"],
        [2, "Comentario"],
        [3, "Otro"]
    ]
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_soporte)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre

class Contacto(models.Model):

    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    correo = models.EmailField()
    telefono = models.CharField(max_length=12)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre

#TABLA PRODUCTO
class Producto(models.Model):
    opciones_producto = [
        [0, "Planta"],
        [1, "Maceta"],
        [2, "Tierra"]
    ]
    id = models.IntegerField(primary_key=True, default=1, verbose_name='Id')
    tipo_producto = models.IntegerField(choices=opciones_producto, default=0)
    nombre_prod = models.CharField(max_length=64, verbose_name='Nombre_prod')
    descripcion1_prod = models.CharField(max_length=100, verbose_name='Descripcion1_prod')
    descripcion2_prod = models.CharField(max_length=100, verbose_name='Descripcion2_prod') #por si se necesita mas detalles
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField( verbose_name='stock')
    imagen = models.ImageField(upload_to="productos",null = True)
    def __str__(self):
        return self.id.__str__()

# Tabla Boleta
class Boleta(models.Model):
    opciones_estado = [
        [0, "En espera"],
        [1, "En camino"],
        [2, "Entregado"],
    ]
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.IntegerField(choices = opciones_estado) 
    fecha = models.DateTimeField(auto_now_add=True, null=True)
    total = models.IntegerField(default=0, verbose_name="total")
    def __str__(self):
        return str(self.id)

#Producto por boleta
class BoletaProducto(models.Model):
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='cantidad')
    def __str__(self):
        return str(self.id_boleta)

class Descuento(models.Model):
    id = models.CharField(primary_key=True, default='', verbose_name='codigo', max_length=24)
    valor_dscto = models.FloatField(verbose_name='valor_dscto')

class Subscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True, null=True)
    vigencia = models.DateField(verbose_name='vigencia', null=True)
    monto_donado = models.IntegerField(verbose_name='Cantidad donada')
    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_cliente)