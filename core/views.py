from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm, UserLoginForm, SoporteForm, ContactoForm
from django.contrib.auth import authenticate, login as login_auth

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