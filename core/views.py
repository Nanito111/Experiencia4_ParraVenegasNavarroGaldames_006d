from django.shortcuts import render

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
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')