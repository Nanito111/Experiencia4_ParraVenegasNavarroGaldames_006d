from rest_framework import serializers
from core.models import Subscripcion
class SubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscripcion
        fields =['id','fecha','vigencia','monto_donado','id_cliente']