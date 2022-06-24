from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .serializers import PlantaSerializer,MacetaSerializer,TierraSerializer
from core.models import Planta,Maceta,Tierra

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def lista_Planta(request):
    if request.method=='GET':
        planta = Planta.objects.all()
        serializer= PlantaSerializer(planta, many=True)
        return Response(serializer.data)

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def lista_Planta(request):
#     if request.method=='GET':
#         planta = Planta.objects.all()
#         serializer= PlantaSerializer(planta, many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         data = JSONParser().parse(request)
#         serializer = PlantaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def lista_Maceta(request):
    if request.method=='GET':
        maceta = Maceta.objects.all()
        serializer= MacetaSerializer(maceta, many=True)
        return Response(serializer.data)
    


@csrf_exempt
@api_view(['GET'])
def lista_Tierra(request):
    if request.method=='GET':
        tierra = Tierra.objects.all()
        serializer= TierraSerializer(tierra, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT'])
def detalle_planta(request, ide):
    try:
        planta = Planta.objects.get(id=ide)
    except Planta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PlantaSerializer(planta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(planta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def detalle_maceta(request, ide):
    try:
        maceta = Maceta.objects.get(id=ide)
    except Maceta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MacetaSerializer(maceta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MacetaSerializer(maceta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def detalle_tierra(request, ide):
    try:
        tierra = Tierra.objects.get(id=ide)
    except Tierra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TierraSerializer(tierra)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TierraSerializer(tierra, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

