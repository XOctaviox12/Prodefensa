from django.contrib import admin
from .models import Descuento, Actividad, Suscripcion


@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

