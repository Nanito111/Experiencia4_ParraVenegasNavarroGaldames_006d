from django.urls import path
from .views import *

urlpatterns = [
    path('lista_subscriptores',lista_subscriptores,name="lista_subscriptores"),
    path('eliminar_subscriptores/<id>',eliminar_subscriptores, name="eliminar_subscriptores"),
]
