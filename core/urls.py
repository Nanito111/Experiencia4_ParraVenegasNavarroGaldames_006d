from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('quienes-somos', quienes_somos, name="quienes_somos"),
    path('tienda', tienda, name="tienda"),
    path('contacto', contacto, name="contacto"),
    path('soporte', soporte, name="soporte"),
    path('login', login, name="login"),
    path('checkout/<id>/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
    path('carrito', carrito, name="carrito"),
    path('process_order/', processOrder, name="process_order"),
    path('register/', register, name="register"),
    path('account', account, name="account"),
    path('editaccount/<id>/', editaccount, name="editaccount"),
    path('deleteaccount/<id>/', deleteaccount, name="deleteaccount"),
    path('ordenes/<id>/', ordenes, name="ordenes"),
    path('boleta/<id>/', boleta, name="boleta"),
    path('subscripcion', subscripcion, name="subscripcion"),
    path('subscriptores', subscriptores, name="subscriptores"),
]