from django.db import models

# Create your models here.

# TABLA CUENTA
class Cuenta(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20, verbose_name='Usuario')
    nombre = models.CharField(max_length=64, blank=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=64, blank=False, verbose_name='Apellido')
    correo = models.CharField(max_length=100, blank=False, verbose_name='Correo')
    password = models.CharField(max_length=50, blank=False, verbose_name='Contraseña')

    def __str__(self):
        return self.usuario