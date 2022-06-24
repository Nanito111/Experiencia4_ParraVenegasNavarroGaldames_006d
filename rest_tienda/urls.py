from django.urls import path
from rest_tienda.views import lista_Planta,lista_Maceta,lista_Tierra,detalle_planta,detalle_maceta,detalle_tierra

urlpatterns = [
    path('lista_Planta',lista_Planta,name="lista_Planta"),
    path('lista_Maceta',lista_Maceta,name="lista_Maceta"),
    path('lista_Tierra',lista_Tierra,name="lista_Tierra"),
    path('detalle_planta/<ide>',detalle_planta,name="detalle_planta"),
    path('detalle_maceta/<ide>',detalle_maceta,name="detalle_maceta"),
    path('detalle_tierra/<ide>',detalle_tierra,name="detalle_tierra"),
]