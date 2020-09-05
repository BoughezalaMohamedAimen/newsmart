from chambres.models import Chambre
from .serializers import ChambreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class ChambresAPI(APIView):
    def get(self,request,format=None):
        chambres=ChambreSerializer(Chambre.objects.all(),many=True)
        return Response(chambres.data, status=200)
