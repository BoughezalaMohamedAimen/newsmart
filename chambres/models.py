from django.db import models
from config.models import Config
import string
import secrets
import hmac
import hashlib


class Chambre(models.Model):
    nom=models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    def __str__(self):
        return self.nom

    @property
    def devices_list(self):
        from chambres.api.serializers import DeviceSerializer
        devices=Device.objects.filter(chambre=self)
        return DeviceSerializer(devices,many=True).data








class Device(models.Model):
    class Type(models.TextChoices):
        lampe="Lampe"
        prise="Prise"
        rideau="Rideau"

    nom=models.CharField(max_length=255)
    type=models.CharField(max_length=255,choices=Type.choices)
    chambre=models.ForeignKey(Chambre,on_delete=models.CASCADE,blank='true')
    etat=models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    @property
    def commandes_list(self):
        from chambres.api.serializers import CommandeSerializer
        commandes=Commande.objects.filter(device=self)
        return CommandeSerializer(commandes,many=True).data





class Commande(models.Model):
    titre=models.CharField(max_length=255)
    commande=models.CharField(max_length=255)
    device=models.ForeignKey(Device,on_delete=models.CASCADE,blank='true')


class Chalenge(models.Model):
    chalenge=models.CharField(max_length=300)
    result=models.CharField(max_length=300)
    ip=models.CharField(max_length=300)
    heure=models.DateTimeField(auto_now_add=True)

    def create(self):
        self.chalenge = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
        cle=str.encode(Config.objects.all().first().cle_local)
        self.result=hmac.new(cle,str.encode(self.chalenge)).hexdigest()
        self.save()
