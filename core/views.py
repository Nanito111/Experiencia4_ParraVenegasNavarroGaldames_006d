from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm, UserLoginForm, SoporteForm, ContactoForm, UserChangeForm, BoletaForm
from django.contrib.auth import authenticate, login as login_auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import BoletaProducto, Descuento, Producto, Boleta, Subscripcion
import json
import datetime
from dateutil.relativedelta import relativedelta


def index(request):
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    if 'subtotal' not in request.session:
        request.session['subtotal'] = 0
    if 'descuento' not in request.session:
        request.session['descuento'] = 0
    
    try:
        Subscripcion.objects.get(id_cliente=request.user)
        if request.session['descuento'] == 0:
            request.session['descuento'] = 5
    except:
        request.session['descuento'] = request.session['descuento']

    print("\n"+request.user.__str__()+"\nCarrito: "+request.session['carrito'].__str__(), "\nSubtotal: "+request.session['subtotal'].__str__(), "\nDescuento: "+request.session['descuento'].__str__()+"\n")
    return render(request, 'core/index.html')

def quienes_somos(request):
    # print(request.session['carrito'])
    return render(request, 'core/quienes_somos.html')

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

#region account

def login(request):
    form = UserLoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(to="index")
    return render(request, 'registration/login.html', {'login_form': form })

def register(request):
    data = {
        'form': RegisterForm(),
        'user_exist': False
    }

    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        
        if formulario.is_valid():
            if User.objects.filter(username = formulario.data['username']).exists() == False:
                formulario.save()
                user = authenticate(username = formulario.data['username'], password = formulario.data['password1'])
                login_auth(request, user)
                messages.success(request, "Usuario creado correctamente")
                #redigir al home
                return redirect(to="index")
        else:
            data['user_exist'] = True
            return render(request, 'registration/register.html', data)
            
        data['form'] = formulario

    return render(request, 'registration/register.html', data)

def account(request):
    datos = {
        "isSub": False,
        "sub": None
    }
    
    try:
        datos['sub'] = Subscripcion.objects.get(id_cliente=request.user)
        datos['isSub'] = True
    except:
        datos['isSub'] = False

    return render(request, 'registration/account.html', datos)

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
def deleteaccount(request, id):
    usuario = User.objects.get(username=id)
    if usuario != request.user:
        return redirect(to="index")
    User.objects.filter(username=id).delete()
    return redirect(to="index")


#endregion

#region e-commerce
def tienda(request):
    productos = Producto.objects.all()

    # del request.session['carrito']

    carrito = request.session['carrito']

    datos = {
        'productos': productos,
        'carrito': carrito
    }
    
    # request.session.setdefault('carrito', [])
    
    # print(request.session['carrito'])
    return render(request, 'tienda/tienda.html', datos)

def updateItem(request):
    data = json.loads(request.body)
    productId = int(data['productId'])
    action = data['action']

    carrito = request.session['carrito']

    print('Action:', action)
    print('productId:', productId)

    if action == 'add':
        if next((item for item in carrito if item['product'] == productId), None) == None:
            carrito += [{'product': productId, 'cantidad': 1}]

    elif action == 'aumentar':
        contador = 0
        for item in carrito:
            if item['product'] == productId:
                break
            contador += 1
        carrito[contador]['cantidad'] += 1
        
    elif action == 'restar':
        contador = 0
        for item in carrito:
            if item['product'] == productId:
                break
            contador += 1
        if carrito[contador]['cantidad'] > 1: 
            carrito[contador]['cantidad'] -= 1

    elif action == 'eliminar':
        contador = 0
        for item in carrito:
            if item['product'] == productId:
                break
            contador += 1
        carrito.pop(contador)
    
    request.session['carrito'] = carrito
    print(request.session['carrito'])
    return JsonResponse('carrito modificado', safe=False)

def carrito(request):
    cartProductos = []
    subtotal = 0
    for i in request.session['carrito']:
        cartProductos.extend(list(Producto.objects.filter(id = i['product'])))

    contador = 0
    for item in request.session['carrito']:
        subtotal = subtotal + getattr(cartProductos[contador], 'precio') * item['cantidad']
        contador += 1

    request.session['subtotal'] = subtotal

    datos = {
            'cartProductos': cartProductos,
            'carrito':request.session['carrito'],
            'alert_cupon': 0}
    
    isSub = False
    try:
        Subscripcion.objects.get(id_cliente=request.user)
        isSub = True
    except:
        isSub = False

    if request.method == 'POST':
        cupon = request.POST['cupon'].strip().upper()
        try:
            valor_dcto = Descuento.objects.get(id=cupon)
            if isSub :
                request.session['descuento'] = getattr(valor_dcto, 'valor_dscto')+5
            else:
                request.session['descuento'] = getattr(valor_dcto, 'valor_dscto')
            datos['alert_cupon'] = 2
        except:
            datos['alert_cupon'] = 1
    
    return render(request, 'tienda/carrito.html', datos)

def processOrder(request):
    data = json.loads(request.body)
    totalcompra = int(data['total'])
    user = User.objects.get(username = data['user'])
    carrito = request.session['carrito']
    fecha = datetime.datetime.utcnow().date()

    boleta = Boleta(id_cliente=user, estado=0, fecha=fecha, total=totalcompra)
    boleta.full_clean()
    boleta.save()

    for item in carrito:
        # latest_id = Entry.objects.latest('id').id
        boletaFK = Boleta.objects.get(id = Boleta.objects.latest('id').id)
        productoFK = Producto.objects.get(id = item['product'])
        productoBoleta = BoletaProducto(id_boleta=boletaFK, id_producto=productoFK, cantidad=item['cantidad'])
        productoBoleta.full_clean()
        productoBoleta.save()

        newStock = getattr(productoFK, 'stock')-item['cantidad']
        setattr(productoFK, 'stock', newStock)
        productoFK.save()
    
    request.session['carrito'] = []
    request.session['subtotal'] = 0
    try:
        Subscripcion.objects.get(id_cliente=request.user)
        request.session['descuento'] = 5
    except:
        request.session['descuento'] = 0
    messages.success(request, "¡Compra Exitosa!")
    return JsonResponse('Payment complete!', safe=False)

def subscripcion(request):
    datos = {
        "isSub": False,
    }
    try:
        Subscripcion.objects.get(id_cliente=request.user)
        datos['isSub'] = True
    except:
        datos['isSub'] = False

    if request.method == 'POST':
        if datos['isSub'] == False:
            opcion = request.POST['btnradio']
            if opcion == "1":
                delta = relativedelta(months=1)
                monto = 2500
            elif opcion == "2":
                delta = relativedelta(months=6)
                monto = 10000
            else:
                delta = relativedelta(months=12)
                monto = 25000

            fecha = datetime.datetime.today() + delta
            request.session['descuento'] = request.session['descuento'] + 5
            user = User.objects.get(username = request.user.username)
            sub = Subscripcion(fecha=datetime.datetime.today(), vigencia=fecha, monto_donado=monto, id_cliente=user)
            sub.full_clean()
            sub.save()
            messages.success(request, "¡Ahora eres un subscriptor!")
            return redirect(to="index")
        else:
            request.session['descuento'] = request.session['descuento'] - 5
            Subscripcion.objects.filter(id_cliente=request.user).delete()
            return redirect(to="index")

    return render(request, 'core/subscripcion.html', datos)

@login_required
def checkout(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        "product": producto,
        "form": BoletaForm
    }
    if request.method == 'POST':
        data = dict(request.POST)
        cantidad = data['cantidadProd'][0]
        direccion = data[''][0]
        telefono = data[''][0]

    return render(request, 'core/checkout.html', datos)

@login_required
def ordenes(request, id):
    user = User.objects.get(username = id)
    if user != request.user:
        return redirect(to="index")

    datos = {
        'orden': Boleta.objects.filter(id_cliente = user)
    }

    return render(request, 'core/ordenes.html' , datos)

@login_required
def boleta(request, id):
    boleta_producto = BoletaProducto.objects.filter(id_boleta=id).values()
    
    contador = 0
    for i in boleta_producto:
        boleta_producto[contador].update({'precio': getattr(Producto.objects.get(id = i['id_producto_id']), 'precio')})
        boleta_producto[contador].update({'nombre' : getattr(Producto.objects.get(id = i['id_producto_id']), 'nombre_prod')})
        contador += 1

    datos = {
        'id_boleta': id,
        'producto_boleta': boleta_producto
    }
    return render(request, 'core/boleta.html', datos)

#endregion
def subscriptores(request):
    return render(request, 'core/subscriptores.html')