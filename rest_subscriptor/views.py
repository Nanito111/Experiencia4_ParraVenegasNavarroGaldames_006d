from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Subscripcion
from .serializers import SubscripcionSerializer
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def lista_subscriptores(request):
    if request.method == 'GET':
        subscrip = Subscripcion.objects.all()
        serializer = SubscripcionSerializer(subscrip,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubscripcionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            Subscripcion.objects.get(id_cliente=request.user)
            request.session['descuento'] = request.session['descuento'] - 5
        except:
            request.session['descuento'] = request.session['descuento']
            
        subscrip = Subscripcion.objects.all()
        subscrip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def eliminar_subscriptores(request, id):
    try:
        sub = Subscripcion.objects.get(id = id)
    except Subscripcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        try:
            Subscripcion.objects.get(id_cliente=request.user)
            request.session['descuento'] = request.session['descuento'] - 5
        except:
            request.session['descuento'] = request.session['descuento']
        sub.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
