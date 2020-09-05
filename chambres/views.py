from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Chalenge,Commande
from django.http import HttpResponse
from config.models import Config
import requests


class NewChalenge(TemplateView):
    def get(self,request):
        chalenge=Chalenge(ip=request.META.get("REMOTE_ADDR"))
        chalenge.create()
        return HttpResponse(chalenge.chalenge)



class ChangeEtat(TemplateView):
    def get(self,request,id):
        try:
            if  self.verify_chalenge(request):
                device=Commande.objects.get(id=id)
                print(commande.titre)
            else:
                return HttpResponse(status=403)
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=500)




    def verify_chalenge(self,request):
        ip=request.META.get("REMOTE_ADDR")
        config=Config.objects.all().first()
        chalenge=Chalenge.objects.last()
        if ip == config.ip or chalenge.result==request.GET.get('ch'):
            Chalenge.objects.filter(ip=ip).delete()
            return True
        else:
            return False
