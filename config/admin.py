from django.contrib import admin
from .models import Config

class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        Can_Add = super().has_add_permission(request)
        if Can_Add and Config.objects.exists():
            Can_Add = False
        return Can_Add

    list_display = ('ip', 'site','identifiant','mot_de_passe','cle_local')


admin.site.register(Config,ConfigAdmin)
