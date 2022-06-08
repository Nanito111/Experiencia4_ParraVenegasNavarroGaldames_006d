from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from core.models import Contacto
from .forms import RegisterForm, EditUserForm, UserLoginForm, SoporteForm, ContactoForm, UserChangeForm, RemoveForm
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
    data = {
        'form': UserLoginForm(),
        'mensaje': "AWWA",
    }

    if request.method == 'POST':
        formulario = UserLoginForm(request.POST)
        
        if formulario.is_valid():
            user = authenticate(username = formulario.data['username'], password = formulario.data['password'])
            if user is not None:
                login_auth(request, user)
                #redigir al home
                return redirect(to="index")
            else:
                data['mensaje'] = "El Usuario o la Contraseña son Incorrectos"
                print(data['mensaje'])
                return render(request, 'registration/login.html', data) 
        else:
            print(data['mensaje'])
            return render(request, 'registration/login.html', data)
                
        
        data["form"] = formulario
    return render(request, 'registration/login.html', data)

def register(request):
    data = {
        'form': RegisterForm(),
        'register_message':""
    }

    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        
        if formulario.is_valid():
            if User.objects.filter(username = formulario.data['username']).exists() == False:
                formulario.save()
                user = authenticate(username = formulario.data['username'], password = formulario.data['password1'])
                login_auth(request, user)
                #redigir al home
                return redirect(to="index")
        else:
            data['register_message'] = "El usuario ya existe"
            return render(request, 'registration/register.html', data)
            
        data['form'] = formulario

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