from django.shortcuts import render, redirect

from core.models import Contacto
from .forms import CustomUserCreationForm, UserLoginForm, SoporteForm, ContactoForm
from django.contrib.auth import authenticate, login as login_auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'core/contacto.html', data)


def soporte(request):
    data = {
        'form': SoporteForm()
    }
    if request.method == 'POST':
        formulario = SoporteForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'core/soporte.html', data)

def login(request):
    data = {
        'form': UserLoginForm()
    }
    return render(request, 'registration/login.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login_auth(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redigir al home
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/register.html', data)

def account(request):
    return render(request, 'registration/account.html')