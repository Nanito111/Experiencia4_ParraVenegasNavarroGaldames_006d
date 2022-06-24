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
    path('register/', register, name="register"),
    path('account', account, name="account"),
    path('editaccount/<id>/', editaccount, name="editaccount"),
    path('deleteaccount/<id>/', deleteaccount, name="deleteaccount"),
    path('ordenes/<id>/', ordenes, name="ordenes")
]