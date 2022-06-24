from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# TABLA CUENTA
# class Cuenta(models.Model):
#     usuario = models.CharField(primary_key=True, max_length=20, verbose_name='Usuario')
#     nombre = models.CharField(max_length=64, blank=False, verbose_name='Nombre')
#     apellido = models.CharField(max_length=64, blank=False, verbose_name='Apellido')
#     correo = models.CharField(max_length=100, blank=False, verbose_name='Correo')
#     password = models.CharField(max_length=50, blank=False, verbose_name='Contraseña')

#     def __str__(self):
#         return self.usuario



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
    id = models.IntegerField(primary_key=True, verbose_name='Id')
    nombre_prod = models.CharField(max_length=64, verbose_name='Nombre_prod')
    descripcion_prod = models.CharField(max_length=100, verbose_name='Descripcion_prod')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField( verbose_name='stock')
    imagen = models.ImageField(upload_to="productos",null = True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.id.__str__()

#Tabla Tierra
class Tierra(Producto):
    tipo = models.CharField(max_length=20, verbose_name='Tipo')

#Tabla Planta
class Planta(Producto):
    toxicidad = models.CharField(max_length=40, verbose_name='Toxicidad')
    alto = models.FloatField(verbose_name='Alto')
    ancho = models.FloatField(verbose_name='Ancho')
    largo = models.FloatField(verbose_name='Largo')

#Tabla Maceta
class Maceta(Producto):
    material = models.CharField(max_length=30, verbose_name='Material')
    alto = models.FloatField(verbose_name='Alto')
    ancho = models.FloatField(verbose_name='Ancho')
    largo = models.FloatField(verbose_name='Largo')