from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from core.models import Contacto
from .forms import CustomUserCreationForm, EditUserForm, UserLoginForm, SoporteForm, ContactoForm, UserChangeForm, RemoveForm
from django.contrib.auth import authenticate, login as login_auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            messages.success(request, "El mensaje ha sido enviado correctamente")
            return redirect(to="index")
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
            messages.success(request, "El mensaje ha sido enviado correctamente")
            return redirect(to="index")
        else:
            data["form"] = formulario
    return render(request, 'core/soporte.html', data)

def login(request):
    return render(request, 'registration/login.html')

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

@login_required
def editaccount(request, id):
    user = User.objects.get(username = id)
    if user != request.user:
        return redirect(to="index")
    datos = {
        "form": UserChangeForm(instance=user)
    }

    if request.method == 'POST':
        formulario = UserChangeForm(data=request.POST, instance=user)

        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Modificados correctamente"
            messages.success(request, "Datos modificados correctamente")
            #redigir al home
            return redirect(to="index")
   
        else:
            print("ERROR")
    return render(request, 'registration/editaccount.html', datos)

@login_required
def deleteaccount (request, id):
    usuario = get_object_or_404(User, username=id)
    if usuario != request.user:
        return redirect(to="index")
    usuario.delete()
    return redirect(to="index")