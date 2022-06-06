from django import forms
from django.forms import ModelForm
from .models import *

class CuentaForm(ModelForm):
    class Meta:
        model = Cuenta
        fields = ['usuario', 'nombre', 'apellido','correo','password']