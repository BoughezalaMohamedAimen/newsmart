from django.contrib import admin
from .models import *



class ChambreAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')


admin.site.register(Chambre,ChambreAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')


admin.site.register(Device,DeviceAdmin)
#
#
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre')


admin.site.register(Commande,CommandeAdmin)
