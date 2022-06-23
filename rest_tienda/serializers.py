from rest_framework import serializers
from core.models import Planta,Maceta,Tierra



class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields ='__all__'

class MacetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maceta
        fields ='__all__'

class TierraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tierra
        fields ='__all__'