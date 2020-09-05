from rest_framework import serializers
from chambres.models import Chambre,Device,Commande


class ChambreSerializer(serializers.ModelSerializer):
    devices=serializers.ReadOnlyField(source='devices_list')
    class Meta:
        model = Chambre
        fields ='__all__'



class DeviceSerializer(serializers.ModelSerializer):
    commandes=serializers.ReadOnlyField(source='commandes_list')
    class Meta:
        model = Device
        fields ='__all__'


class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields ='__all__'
