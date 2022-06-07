from dataclasses import fields
from urllib.request import Request
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def soporte(request):
    return render(request, 'core/soporte.html')

def login(request):
    state = {"error_alert":""}
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        if Cuenta.objects.filter(usuario = username).exist():
            state['error_alert'] = "SESION LISTA"
            return render(request, 'core/register.html', state)
        else:
            state['error_alert'] = "Usuario o Contraseña Incorrectos"
            return render(request, 'core/register.html', state)

    return render(request, 'core/login.html', state)

def register(request):
    state = {"register_message":""}
    if request.method == 'POST':
        formulario = CuentaForm(request.POST)
        if formulario.is_valid:
            username = formulario.data['usuario']
            if Cuenta.objects.filter(usuario = username).exists():
                state['register_message'] = "El usuario ya existe"
                return render(request, 'core/register.html', state)
            else:
                formulario.save()
                return redirect(to="login")
    return render(request, 'core/register.html', state)