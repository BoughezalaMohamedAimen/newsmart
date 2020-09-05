from django.urls import path,re_path,include
from .views import *
from .api.api_views import ChambresAPI

urlpatterns = [
    path('api',ChambresAPI.as_view(),name="ChambresAPI" ),
    path('chalenge',NewChalenge.as_view(),name='NewChalenge'),
    path('commande/<int:id>/',ChangeEtat.as_view(),name='ChangeEtat'),
]
